(ns advent-of-code.2015.3
  (:require [advent-of-code.util :as util]))

(defn deliver [[x y] direction]
  (case direction
    \< [(dec x) y]
    \> [(inc x) y]
    \^ [x (inc y)]
    \v [x (dec y)]))

(defn build-map [directions]
  (loop [directions directions visits [[0 0]]]
    (if (empty? directions)
      visits
      (recur (rest directions)
             (conj visits (deliver (peek visits) (first directions)))))))

(defn part1 []
  (let [directions (util/load-input-string 2015 3)]
    (count (set (build-map directions)))))

(defn part2 []
  (let [directions (util/load-input-string 2015 3)]
    (count
     (set
      (concat (build-map (take-nth 2 directions))
              (build-map (take-nth 2 (rest directions))))))))
