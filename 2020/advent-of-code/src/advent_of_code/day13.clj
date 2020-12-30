(ns advent-of-code.day13
  (:require [advent-of-code.util :as util]))

;; Part 1

(def departure-time 1001287)
(def bus-ids [13 37 461 17 19 29 739 41 23])

(defn find-departure-time [earliest-departure-time bus-id]
  (loop [time 0]
    (if (>= time earliest-departure-time)
      time
      (recur (+ time bus-id)))))

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

(def sample-buses
  [{:offset 0 :cycle 7}
   {:offset 1 :cycle 13}
   {:offset 4 :cycle 59}
   {:offset 6 :cycle 31}
   {:offset 7 :cycle 19}])

(def input-buses
  [{:offset 0 :cycle 13}
   {:offset 7 :cycle 37}
   {:offset 13 :cycle 461}
   {:offset 27 :cycle 17}
   {:offset 32 :cycle 19}
   {:offset 42 :cycle 29}
   {:offset 44 :cycle 739}
   {:offset 54 :cycle 41}
   {:offset 67 :cycle 23}])

(defn f [x offset cycle lcm]
  (loop [x x]
    (if (zero? (mod (+ x offset) cycle))
      x
      (recur (+ x lcm)))))

(defn part2 []
  (let [buses input-buses]
    (loop [[bus & buses-rest] (rest buses) x 0 lcm (:cycle (first buses))]
      (if (nil? bus)
        x
        (recur buses-rest
               (f x (:offset bus) (:cycle bus) lcm)
               (* lcm (:cycle bus)))))))

