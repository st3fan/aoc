(ns advent-of-code.day12p2
  (:require [advent-of-code.util :as util]))

(defn N [ferry v]
  (update ferry :wy + v))

(defn S [ferry v]
  (update ferry :wy - v))

(defn E [ferry v]
  (update ferry :wx + v))

(defn W [ferry v]
  (update ferry :wx - v))

(defn F [ferry v]
  (let [dx (* v (:wx ferry)) dy (* v (:wy ferry))]
    (-> ferry
        (update :x + dx)
        (update :y + dy))))

(defn- rotate-point [[wx wy] degrees]
  (case degrees
      0 [   wx     wy]
     90 [   wy  (- wx)]
    180 [(- wx) (- wy)]
    270 [(- wy)    wx]))

(defn R [ferry v]
  (let [[wx wy] (rotate-point [(:wx ferry) (:wy ferry)] v)]
    (assoc ferry :wx wx :wy wy)))

(defn L [ferry v]
  (let [[wx wy] (rotate-point [(:wx ferry) (:wy ferry)] (- 360 v))]
    (assoc ferry :wx wx :wy wy)))

;;

(defn execute-ferry-instruction [ferry [op arg]]
  ((resolve (symbol op)) ferry arg))

(defn move-ferry [ferry instructions]
  (loop [[instruction & rest] instructions ferry ferry]
    (if-not instruction
      ferry
      (recur rest (execute-ferry-instruction ferry instruction)))))

(defn create-ferry []
  {:x 0 :y 0 :wx 10 :wy 1 :wq 0})

;;

(defn parse-instruction [ins]
  (let [[_ op arg] (re-matches #"(\w)(\d+)" ins)]
    [op (Integer/parseInt arg)]))

(defn load-instructions []
  (util/load-input 2020 12 parse-instruction))

;;

(defn part2 []
  (let [ferry (move-ferry (create-ferry) (load-instructions))]
    (+ (Math/abs (:x ferry)) (Math/abs (:y ferry)))))
