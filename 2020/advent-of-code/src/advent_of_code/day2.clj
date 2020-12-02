(ns advent-of-code.day2
  (:require [advent-of-code.util :as util]))

(defn parse-input [line]
  (if-let [matches (re-matches #"(\d+)-(\d+) (.): (.+)" line)]
    [(Integer/parseInt (nth matches 1))
     (Integer/parseInt (nth matches 2))
     (first (char-array (nth matches 3))) ;; Ouch
     (nth matches 4)]))

(defn check-policy-1 [[min max letter password]]
  (let [count (util/count-characters password letter)]
    (and (>= count min)
         (<= count max))))

(defn check-policy-2 [[posa posb letter password]]
  (util/xor (= letter (nth password (dec posa)))
            (= letter (nth password (dec posb)))))

(defn part1 []
  (count (filter check-policy-1 (util/load-input 2 parse-input))))

(defn part2 []
  (count (filter check-policy-2 (util/load-input 2 parse-input))))
