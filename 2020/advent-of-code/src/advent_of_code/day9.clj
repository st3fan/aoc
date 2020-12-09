(ns advent-of-code.day9
  (:require [advent-of-code.util :as util]
            [clojure.math.combinatorics :as combo]))

(defn load-input []
  (vec (util/load-input 2020 9 #(Long/parseLong %))))

;;

(defn has-sum-pair [coll n]
  (some #(= (apply + %) n) (combo/permuted-combinations coll 2)))

(defn some-test [preamble numbers]
  (filter #(has-sum-pair preamble %) numbers))

(defn find-first-mismatch [input preamble-size]
  (loop [preamble (subvec input 0 preamble-size) numbers (subvec input preamble-size)]
    (when-not (empty? numbers)
      (if-not (has-sum-pair preamble (first numbers))
        (first numbers)
        (recur (conj (vec (rest preamble)) (first numbers))
               (rest numbers))))))

(defn part1 []
  (let [input (load-input)]
    (find-first-mismatch input 25)))

;;

(defn find-summed-list-1 [input target]
  (loop [input input numbers []]
    (when-not (empty? input)
      (if (and (> (count numbers) 1)
               (= (apply + numbers) target))
        numbers
        (recur (rest input)
               (conj numbers (first input)))))))

(defn find-summed-list [input target]
  (loop [input input]
    (println input)
    (when-not (empty? input)
      (if-let [numbers (find-summed-list-1 (vec input) target)]
        (+ (apply min numbers) (apply max numbers))
        (recur (rest input))))))

(defn part2 []
  (let [input (load-input) secret (find-first-mismatch input 25)]
    (find-summed-list input secret)))
