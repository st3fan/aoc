(ns advent-of-code.2019.day12
  (:require [advent-of-code.util :as util]
            [clojure.math.combinatorics :as combo]))

(defn parse-moon [line]
  (if-let [matches (re-matches #"<x=(.+?), y=(.+?), z=(.+?)>" line)]
    {:p {:x (Integer/parseInt (nth matches 1))
         :y (Integer/parseInt (nth matches 2))
         :z (Integer/parseInt (nth matches 3))}
     :v {:x 0
         :y 0
         :z 0}}))

(defn load-system []
  {:iteration 0
   :moons (vec (util/load-input 2019 12 parse-moon))})

(defn velocity-change [a b axis]
  (- (compare (get-in a [:p axis]) (get-in b [:p axis]))))

(defn moon-apply-gravity [a b]
  (-> a
      (update-in [:v :x] + (velocity-change a b :x))
      (update-in [:v :y] + (velocity-change a b :y))
      (update-in [:v :z] + (velocity-change a b :z))))

(defn system-apply-gravity [system]
  (loop [indexes (combo/permuted-combinations (range (count (:moons system))) 2) system system]
    (if (empty? indexes)
      system
      (let [[ai bi] (first indexes)]
        (let [updated-moon (moon-apply-gravity (nth (:moons system) ai) (nth (:moons system) bi))]
          (recur
           (rest indexes)
           (assoc-in system [:moons ai] updated-moon)))))))

(defn moon-apply-velocity [moon]
  (-> moon
      (update-in [:p :x] + (get-in moon [:v :x]))
      (update-in [:p :y] + (get-in moon [:v :y]))
      (update-in [:p :z] + (get-in moon [:v :z]))))

(defn simulate-motion [system]
  (let [system (update system :iteration inc)]
    (let [system (system-apply-gravity system)]
      (assoc system :moons (mapv moon-apply-velocity (:moons system))))))

;; TODO This was nicer
;; (->> (update system :iteration inc)
;;      (system-apply-gravity)
;;      (mapv moon-apply-velocity)))

(defn moon-kinetic-energy [moon]
  (* (+ (Math/abs (:x (:p moon))) (Math/abs (:y (:p moon))) (Math/abs (:z (:p moon))))
     (+ (Math/abs (:x (:v moon))) (Math/abs (:y (:v moon))) (Math/abs (:z (:v moon))))))

(defn moon-kinetic-energy [moon]
  (* (apply + (map #(Math/abs (get-in moon [:p %])) [:x :y :z]))
     (apply + (map #(Math/abs (get-in moon [:v %])) [:x :y :z]))))

(defn system-kinetic-energy [system]
  (reduce + (map moon-kinetic-energy (:moons system))))

(defn part1 []
  (let [system (load-system)]
    (system-kinetic-energy (last (take 1001 (iterate simulate-motion system))))))

;;

(defn velocity-axis-zero? [system axis]
  (every? #(zero? (get-in % [:v axis])) (:moons system)))

(defn iterations-until-zero [system axis]
  (->> system
       (iterate simulate-motion)
       (rest)
       (filter #(velocity-axis-zero? % axis))
       (first)
       :iteration))

(defn part2 []
  (let [system (load-system)]
    (apply * (map #(iterations-until-zero system %) [:x :y :z]))))
