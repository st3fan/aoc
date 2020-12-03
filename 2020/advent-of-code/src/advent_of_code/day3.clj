(ns advent-of-code.day3
  (:require [advent-of-code.util :as util]))

(defn load-map []
  (let [input (doall (util/load-input 3 seq))]
    {:data  input
     :width (count (first input))
     :height (count input)}))

(defn at-bottom [map y]
  (>= y (:height map)))

(defn has-tree [map x y]
  (let [line (nth (:data map) y)]
    (= \# (nth line (mod x (:width map))))))

(defn encountered-trees [map [slope-x slope-y]]
  (loop [x 0 y 0 c 0]
    (if (at-bottom map y)
      c
      (recur (+ x slope-x) (+ y slope-y) (+ c (if (has-tree map x y) 1 0))))))

(defn part1 []
  (let [map (load-map)]
    (encountered-trees map [3 1])))

(defn part2 []
  (let [m (load-map) slopes [[1 1] [3 1] [5 1] [7 1] [1 2]]]
    (apply * (map #(encountered-trees m %) slopes))))
