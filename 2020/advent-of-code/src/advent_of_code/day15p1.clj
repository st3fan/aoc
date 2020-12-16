(ns advent-of-code.day15
  (:require [advent-of-code.util :as util]
            [clojure.string :as string]))

(def starting-numbers [8,0,17,4,1,12])

(defn index-of [v n]
  (let [index (.indexOf v n)]
    (if (neg? index)
      nil
      index)))

(defn next-number [[number & numbers]]
  (if-let [index (index-of numbers number)]
    (- (inc (count numbers)) (- (count numbers) index))
    0))

(defn nth-number-spoken [starting-numbers n]
  (loop [spoken (reverse starting-numbers)]
    (if (= (count spoken) n)
      (first spoken)
      (recur (cons (next-number spoken) spoken)))))

(nth-number-spoken [0 3 6] 2020)
(time (nth-number-spoken [0 3 6] 10000))

;;

(defn last-seen [v n]
  (let [index (.indexOf v n)]
    (if (neg? index)
      nil
      index)))

(last-seen [0 3 6])

(let [v [1 5 7 10 20 30 30]
      c (count v)]
  (.lastIndexOf v 30))

(defn next-number [numbers]
  (let [number (peek numbers)
        c (count numbers)
        index (.lastIndexOf numbers number c)]
    (if (= index (dec (count numbers)))
      0
      (- (count numbers) index))))

(next-number [0 3 6 0 4 0])

(defn nth-number-spoken [starting-numbers n]
  (loop [spoken starting-numbers]
    (if (= (count spoken) n)
      (peek spoken)
      (recur (conj (next-number spoken) spoken)))))

(nth-number-spoken [0 3 6] 2020)
(time (nth-number-spoken [0 3 6] 10000))


(defn part1 []
  (nth-number-spoken starting-numbers 30000000))

