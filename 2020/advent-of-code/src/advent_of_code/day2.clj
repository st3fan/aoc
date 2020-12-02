(ns advent-of-code.day2
  (:require [clojure.java.io :as io]))

;; Horrible code alert!

(defn xor [a b] ;; TODO This should be a macro
  (and (or a b)
       (not= a b)))

(defn count-characters [s c]
  (let [c (first (char-array c))]
    (->> s
         (filter (partial = c))
         count)))

(defn check-policy-1 [policy]
  (if-let [matches (re-matches #"(\d+)-(\d+) (.): (.+)" policy)]
    (let [min (Integer/parseInt (nth matches 1))
          max (Integer/parseInt (nth matches 2))
          letter (nth matches 3)
          password (nth matches 4)]
      (let [count (count-characters password letter)]
        (and (>= count min)
             (<= count max))))))

(defn check-policy-2 [policy]
  (if-let [matches (re-matches #"(\d+)-(\d+) (.): (.+)" policy)]
    (let [posa (Integer/parseInt (nth matches 1))
          posb (Integer/parseInt (nth matches 2))
          letter (nth matches 3)
          password (nth matches 4)]
      (xor (= letter (str (nth password (dec posa))))
           (= letter (str (nth password (dec posb))))))))

(defn part1 []
  (let [input (line-seq (io/reader (io/resource (str "advent_of_code/day2/input"))))]
    (count (filter true? (map check-policy-1 input)))))

(defn part2 []
  (let [input (line-seq (io/reader (io/resource (str "advent_of_code/day2/input"))))]
    (count (filter true? (map check-policy-2 input)))))
