(ns advent-of-code.day11
  (:require [advent-of-code.util :as util]))

(def test-input
  ["L.LL.LL.LL"
   "LLLLLLL.LL"
   "L.L.L..L.."
   "LLLL.LL.LL"
   "L.LL.LL.LL"
   "L.LLLLL.LL"
   "..L.L....."
   "LLLLLLLLLL"
   "L.LLLLLL.L"
   "L.LLLLL.LL"])

(defn load-test-seats []
  (let [input (mapv seq test-input)]
    {:data   (vec (apply concat input))
     :width  (count (first input))
     :height (count input)}))

;;

(defn load-seats []
  (let [input (util/load-input 2020 11 seq)]
    {:data   (vec (apply concat input))
     :width  (count (first input))
     :height (count input)}))

(defn seat-index [seats x y]
  (if (and (>= x 0) (< x (:width seats)) (>= y 0) (< y (:height seats)))
    (+ (* y (:width seats)) x)))

(defn get-seat [seats x y]
  (get (:data seats) (seat-index seats x y)))

(defn set-seat [seats x y v]
  (assoc-in seats [:data (seat-index seats x y)] v))

;; Nested loop/recur is awful.
(defn map-seats [original-seats fn]
  (loop [[y & rest] (range (:height original-seats)) seats original-seats]
    (if-not y
      seats
      (recur rest (loop [[x & rest] (range (:width original-seats)) seats seats]
                    (if-not x
                      seats
                      (recur rest (set-seat seats x y (fn original-seats x y)))))))))

;;

(defn flip-seats-until-stable [seats rules]
  (loop [a (map-seats seats rules) b (map-seats a rules)]
    (if (= a b)
      b
      (let [a (map-seats b rules) b (map-seats a rules)]
        (recur a b)))))

;;

(defn occupied-adjacent-seats [seats x y]
  (let [r [(get-seat seats (- x 1) (- y 1))
           (get-seat seats (- x 0) (- y 1))
           (get-seat seats (+ x 1) (- y 1))
           (get-seat seats (- x 1) (- y 0))
           (get-seat seats (+ x 1) (- y 0))
           (get-seat seats (- x 1) (+ y 1))
           (get-seat seats (- x 0) (+ y 1))
           (get-seat seats (+ x 1) (+ y 1))]]
    (count (filter #{\#} r))))

(defn rules-v1 [seats x y]
  (let [v (get-seat seats x y)]
    (cond (and (= v \L) (= (occupied-adjacent-seats seats x y) 0)) \#
          (and (= v \#) (> (occupied-adjacent-seats seats x y) 3)) \L
          :else v)))

(defn part1 []
  (get (frequencies (:data (flip-seats-until-stable (load-seats) rules-v1))) \#))

;;

(defn has-visible-seat [seats x y dx dy]
  (loop [x (+ x dx) y (+ y dy)]
    (let [v (get-seat seats x y)]
      (if (or (nil? v) (= \L v))
        false
        (if (= v \#)
          true
          (recur (+ x dx) (+ y dy)))))))

(defn visible-seats [seats x y]
  (let [r [(has-visible-seat seats x y -1  1)
           (has-visible-seat seats x y  0  1)
           (has-visible-seat seats x y  1  1)
           (has-visible-seat seats x y -1  0)
           (has-visible-seat seats x y  1  0)
           (has-visible-seat seats x y -1 -1)
           (has-visible-seat seats x y  0 -1)
           (has-visible-seat seats x y  1 -1)]]
    (count (filter true? r))))

(defn rules-v2 [seats x y]
  (let [v (get-seat seats x y)]
    (cond (and (= v \L) (= (visible-seats seats x y) 0)) \#
          (and (= v \#) (> (visible-seats seats x y) 4)) \L
          :else v)))

(defn part2 []
  (get (frequencies (:data (flip-seats-until-stable (load-seats) rules-v2))) \#))
