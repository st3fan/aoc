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
  (+ (* y (:width seats)) x))

(defn get-seat [seats x y]
  (if (and (>= x 0) (< x (:width seats)) (>= y 0) (< y (:height seats)))
    (get (:data seats) (seat-index seats x y))))

(defn set-seat [seats x y v]
  (assoc-in seats [:data (seat-index seats x y)] v))

(defn map-seats [original-seats fn]
  (loop [[y & rest] (range (:height original-seats)) seats original-seats]
    (if-not y
      seats
      (recur rest (loop [[x & rest] (range (:width original-seats)) seats seats]
                    (if-not x
                      seats
                      (recur rest (set-seat seats x y (fn original-seats x y)))))))))

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

;;

(defn apply-rules [seats x y]
  (let [v (get-seat seats x y)]
    (cond
      (and (= v \L) (= (occupied-adjacent-seats seats x y) 0)) \#
      (and (= v \#) (> (occupied-adjacent-seats seats x y) 3)) \L
      :else v)))

(defn flip-seats-until-stable [seats]
  (loop [a (map-seats seats apply-rules) b (map-seats a apply-rules)]
    (if (= a b)
      b
      (let [a (map-seats a apply-rules) b (map-seats a apply-rules)]
        (recur a b)))))

(defn part1 []
  (get (frequencies (:data (flip-seats-until-stable (load-seats)))) \#))
