(ns sonar-sweep.core
  (:require [clojure.java.io :as io]))

(defn load-input [path transformer]
  (->> (io/resource path)
       io/reader
       line-seq
       (mapv transformer)))

(defn part1 []
  (let [input (load-input "input.txt" #(Long/parseLong %))]
    (count (filter #(< (first %) (last %)) (partition 2 1 input)))))

(defn part2 []
  (let [input (load-input "input.txt" #(Long/parseLong %))]
    (count (filter #(< (first %) (last %)) (partition 4 1 input)))))
