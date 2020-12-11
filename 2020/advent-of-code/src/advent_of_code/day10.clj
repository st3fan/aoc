(ns advent-of-code.day9
  (:require [advent-of-code.util :as util]
            [clojure.math.combinatorics :as combo]))

(defn load-input []
  (util/load-input 2020 10 #(Long/parseLong %)))

(def test-adapters-1 [16 10 15 5 1 11 7 19 6 12 4])

(def test-adapters-2 [28 33 18 42 31 14 46 20 48 47 24 23 49 45 19 38
                      39 11 1 32 25 35 8 17 7 9 4 2 34 10 3])

(defn matching-adapter [adapters rating]
  (first (filter #(<= % (+ rating 3)) (sort adapters))))

(defn jolt-distribution [jolts]
  (frequencies (map #(* -1 (apply - %)) (partition 2 1 jolts))))

(defn order-adapters [input]
  (loop [adapters (set input) result [0]]
    (if (empty? adapters)
      (conj result (+ 3 (apply max input)))
      (if-let [adapter (matching-adapter adapters (last result))]
        (recur
         (clojure.set/difference adapters #{adapter})
         (conj result adapter))))))

;;

(defn part1 []
  (let [distribution (-> (load-input) (order-adapters) (jolt-distribution))]
    (* (get distribution 1) (get distribution 3))))

;;

(defn part2 []
  0)
