(ns advent-of-code.day24
  (:require [advent-of-code.util :as util]
            [clojure.math.combinatorics :as combo]))

(def direction->vector
  {"e" [2 0] "se" [1 -1] "ne" [1 1]
   "w" [-2 0] "sw" [-1 -1] "nw" [-1 1]})

(defn parse-line [line]
  (map #(direction->vector (first %)) (re-seq #"(e|se|sw|w|nw|ne)" line)))

(defn sum-vectors [vectors]
  (reduce #(vector (+ (first %1) (first %2)) (+ (second %1) (second %2))) vectors))

(defn load-input []
  (util/load-input 2020 24 #(sum-vectors (parse-line %))))

(defn load-test-input []
  (util/load-test-input 2020 24 #(sum-vectors (parse-line %))))

;; Part 1

(let [points (load-input)]
  (loop [[p & rest-p] points result #{}]
    (if-not p
      (count result)
      (if (contains? result p)
        (recur rest-p (disj result p))
        (recur rest-p (conj result p))))))

;; Part 2

;; Doing the lazy thing here again and model the floor with a map
;; because checking neighbours is then a simple lookup.

(defn create-floor []
  (into {} (map #(vector % false) (combo/cartesian-product (range -200 200) (range -200 200)))))

(defn insert-tiles [floor points]
  (loop [[p & rest-p] points result floor]
    (if-not p
      result
      (if (get result p)
        (recur rest-p (assoc result p false))
        (recur rest-p (assoc result p true))))))

(defn count-neighbours [floor [x y]]
  (let [r [(get floor [(- x 1) (- y 1)])
           (get floor [(- x 1) (+ y 1)])
           (get floor [(- x 2) (- y 0)])
           (get floor [(+ x 2) (- y 0)])
           (get floor [(+ x 1) (- y 1)])
           (get floor [(+ x 1) (+ y 1)])]]
    (count (filter true? r))))

(defn cycle-floor [floor]
  (loop [[[k v] & rest-floor] floor result floor]
    (if-not k
      result
      (let [n (count-neighbours floor k)]
        (if v
          (if (or (= 0 n) (> n 2))
            (recur rest-floor (assoc result k false))
            (recur rest-floor result))
          (if (= 2 n)
            (recur rest-floor (assoc result k true))
            (recur rest-floor result)))))))

(defn count-black-tiles [floor]
  (->> floor vals (filter true?) (count)))

(defn part2 []
  (let [floor (insert-tiles (create-floor) (load-input))]
    (count-black-tiles (nth (iterate cycle-floor floor) 100))))
