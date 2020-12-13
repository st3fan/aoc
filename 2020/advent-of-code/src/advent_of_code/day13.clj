(ns advent-of-code.day13
  (:require [advent-of-code.util :as util]))

(def departure-time 1001287)
(def bus-ids [13 37 461 17 19 29 739 41 23])

(defn find-departure-time [earliest-departure-time bus-id]
  (loop [time 0]
    (if (>= time earliest-departure-time)
      time
      (recur (+ time bus-id)))))

;; Part 1

(defn final-answer [arrival-time s]
  (* (:bus-id s) (- (:time s) arrival-time)))

(defn part1[]
  (let [arrival-time 1001287] ;; Copied from input
    (->> bus-ids
         (map #(assoc {} :bus-id % :time (find-departure-time arrival-time %)))
         (sort-by :time)
         first
         (final-answer arrival-time))))

;; Part 2

(defn part2 []
  0)
