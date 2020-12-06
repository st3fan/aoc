(ns advent-of-code.day6
  (:require [clojure.set]
            [advent-of-code.util :as util]))

(defn load-input []
  (->> (util/load-input 2020 6 set)
       (partition-by empty?)
       (filter (complement empty?))))

(defn part1 []
  (let [input (load-input)]
    (apply + (map #(count (apply clojure.set/union %)) input))))

(defn part2 []
  (let [input (load-input)]
    (apply + (map #(count (apply clojure.set/intersection %)) input))))
