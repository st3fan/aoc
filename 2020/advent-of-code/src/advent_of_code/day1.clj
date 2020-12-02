(ns advent-of-code.day1
  (:require [advent-of-code.util :as util]
            [clojure.math.combinatorics :as combo]))

(defn find-sum [data n c]
  (->> (combo/permuted-combinations data c)
       (filter #(= n (apply + %)))
       (first)
       (apply *)))

(defn part1 []
  (find-sum (util/load-input 1 #(Integer/parseInt %)) 2020 2))

(defn part2 []
  (find-sum (util/load-input 1 #(Integer/parseInt %)) 2020 3))
