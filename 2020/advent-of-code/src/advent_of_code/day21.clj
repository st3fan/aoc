(ns advent-of-code.day21
  (:require [advent-of-code.util :as util]))

(defn parse-line [line]
  (if-let [[_ ingredients allergens] (re-matches #"(.+) \(contains (.+)\)" line)]
    (let [ingredients (clojure.string/split ingredients #" ") allergens (clojure.string/split allergens #", ")]
      {:ingredients (set ingredients) :allergens (set allergens)})))

(defn parse-input []
  nil)

(defn parse-test-input []
  (util/load-test-input 2020 21 parse-line))


(defn eliminate-ingredients [foods]
  (let [allergens (apply clojure.set/union (map :allergens foods))]
    fuuu))

(eliminate-ingredients (parse-test-input))

