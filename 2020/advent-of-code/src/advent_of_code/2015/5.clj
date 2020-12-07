(ns advent-of-code.2015.5
  (:require [advent-of-code.util :as util]))

(defn nice1? [s]
  (and (>= (count (re-seq #"[aeiou]" s)) 3)
       (>= (count (re-seq #"(.)\1" s)) 1)
       (nil? (re-seq #"(ab|cd|pq|xy)" s))))

(defn part1 []
  (let [input (util/load-input 2015 4)]
    (count (filter nice1? input))))

(defn nice2? [s]
  (and (re-seq #"(..).*\1" s)
       (re-seq #"(.).\1" s)))

(defn part2 []
  (let [input (util/load-input 2015 4)]
    (count (filter nice2? input))))
