(ns advent-of-code.2015.2
  (:require [advent-of-code.util :as util]))

(defn parse-int [s]
  (Integer/parseInt s))

(defn paper-required [[l w h]]
  (let [a (* l w) b (* w h) c (* h l)]
    (+ (* 2 (+ a b c)) (min a b c))))

(defn part1 []
  (let [input (util/load-input 2015 2 #(map parse-int (clojure.string/split % #"x")))]
    (apply + (map paper-required input))))

(defn ribbon-required [dimensions]
  (let [[a b] (sort dimensions)]
    (+ (+ a a b b)
       (apply * dimensions))))

(defn part2 []
  (let [input (util/load-input 2015 2 #(map parse-int (clojure.string/split % #"x")))]
    (apply + (map ribbon-required input))))
