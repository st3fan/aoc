(ns advent-of-code.2015.6
  (:require [advent-of-code.util :as util]
            [clojure.math.combinatorics :as combo]))

(defn parse-instruction [s]
  (let [[_ action sx sy ex ey] (re-matches #".*(on|off|toggle) (\d+),(\d+) through (\d+),(\d+)" s)]
    [(keyword action)
     (Integer/parseInt sx)
     (Integer/parseInt sy)
     (Integer/parseInt ex)
     (Integer/parseInt ey)]))

;; This is very slow - is there a faster way to update a vector?

(defn create-grid [width height]
  (vec (repeat (* width height) 0)))

(defn change-light [grid [x y] fn]
  (update grid (+ (* y 1000) x) fn))

(defn change-lights [grid [_ sx sy ex ey] fn]
  (loop [positions (combo/cartesian-product (range sx (inc ex)) (range sy (inc ey))) grid grid]
    (if (empty? positions)
      grid
      (recur (rest positions)
             (change-light grid (first positions) fn)))))

;;

(defn apply-instruction-1 [grid instruction]
  (change-lights grid instruction (case (first instruction)
                                  :on (fn [v] 1)
                                  :off (fn [v] 0)
                                  :toggle (fn [v] (if (zero? v) 1 0)))))

(defn apply-instructions-1 [grid instructions]
  (loop [instructions instructions grid grid]
    (if (empty? instructions)
      grid
      (recur (rest instructions) (apply-instruction-1 grid (first instructions))))))

(defn part1 []
  (let [instructions (util/load-input 2015 6 parse-instruction)
        grid (apply-instructions-1 (create-grid 1000 1000) instructions)]
    (count (filter (complement zero?) grid))))

;;

(defn apply-instruction-2 [grid instruction]
  (change-lights grid instruction (case (first instruction)
                                  :on (fn [v] (inc v))
                                  :off (fn [v] (max 0 (dec v)))
                                  :toggle (fn [v] (+  v 2)))))

(defn apply-instructions-2 [grid instructions]
  (loop [instructions instructions grid grid]
    (if (empty? instructions)
      grid
      (recur (rest instructions) (apply-instruction-2 grid (first instructions))))))

(defn part2 []
  (let [instructions (util/load-input 2015 6 parse-instruction)
        grid (apply-instructions-2 (create-grid 1000 1000) instructions)]
    (apply + grid)))
