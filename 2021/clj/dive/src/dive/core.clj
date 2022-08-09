(ns dive.core
  (:require [clojure.java.io :as io]
            [clojure.core.match :as match]))

(defn load-input [path transformer]
  (->> (io/resource path)
       io/reader
       line-seq
       (mapv transformer)))

(defn transform-line [line]
  "Parse a line into a command (keyword) and units (number)"
  (let [[command units] (clojure.string/split line #"\s+")]
    [(keyword command) (Long/parseLong units)]))

(defn part1 []
  (let [input (load-input "input.txt" transform-line)]
    (loop [input input position 0 depth 0]
      (if (empty? input)
        (* position depth)
        (let [[position-delta depth-delta] (match/match (first input)
                                             [:forward units] [units 0]
                                             [:up units] [0 (- units)]
                                             [:down units] [0 units])]
          (recur (next input) (+ position position-delta) (+ depth depth-delta)))))))

(defn part2 []
  (let [input (load-input "input.txt" transform-line)]
    (loop [input input position 0 depth 0 aim 0]
      (if (empty? input)
        (* position depth)
        (let [[position-delta depth-delta aim-delta] (match/match (first input)
                                                       [:forward units] [units (* aim units) 0]
                                                       [:up units] [0 0 (- units)]
                                                       [:down units] [0 0 units])]
          (recur (next input)
                 (+ position position-delta)
                 (+ depth depth-delta)
                 (+ aim aim-delta)))))))
