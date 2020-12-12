(ns advent-of-code.day12p1
  (:require [advent-of-code.util :as util]))

(defn N [ferry v]
  (update ferry :y + v))

(defn S [ferry v]
  (update ferry :y - v))

(defn E [ferry v]
  (update ferry :x + v))

(defn W [ferry v]
  (update ferry :x - v))

(def directions {0 N, 90 E, 180 S, 270 W})

(defn F [ferry v]
  ((get directions (:a ferry)) ferry v))

(defn R [ferry v]
  (let [a (mod (+ (:a ferry) v) 360)]
    (assoc ferry :a a)))

(defn L [ferry v]
  (let [a (mod (- (:a ferry) v) 360)]
    (assoc ferry :a a)))

(defn execute-ferry-instruction [ferry [op arg]]
  ((resolve (symbol op)) ferry arg))

(defn move-ferry [ferry instructions]
  (loop [[instruction & rest] instructions ferry ferry]
    (println ferry)
    (if-not instruction
      ferry
      (recur rest (execute-ferry-instruction ferry instruction)))))

(defn create-ferry []
  {:a 90 :x 0 :y 0})

;;

(defn parse-instruction [ins]
  (let [[_ op arg] (re-matches #"(\w)(\d+)" ins)]
    [op (Integer/parseInt arg)]))

(defn load-instructions []
  (util/load-input 2020 12 parse-instruction))

;;

(defn part1 []
  (let [ferry (move-ferry (create-ferry) (load-instructions))]
    (+ (Math/abs (:x ferry)) (Math/abs (:y ferry)))))
