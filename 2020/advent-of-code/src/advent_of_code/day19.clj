(ns advent-of-code.day19
  (:require [advent-of-code.util :as util]
            [clojure.string :as string]))

(defn parse-rule [rule]
  (if-let [[_ c] (re-matches #" \"([ab])\"" rule)]
    c
    (if-let [[matches] (re-matches #"(\s(\d+))+" rule)]
      (map #(Integer/parseInt %) (string/split (string/trim matches) #" "))
      (if-let [[_ a b] (re-matches #"((?:\s\d+)+)\s\|((?:\s\d+)+)" rule)]
        (flatten ["(" (parse-rule a) "|" (parse-rule b) ")"])))))

;;(mapv #(Integer/parseInt %) (string/split (string/trim matches) #" "))

(re-matches #"((?:\s\d+)+)\s\|((?:\s\d+)+)" " 1 2 | 3 4")

(defn parse-line [line]
  (println line)
  (if-let [[_ number rule] (re-matches #"(\d+):(.*)" line)]
    [(Integer/parseInt number) (parse-rule rule)]))

(re-matches #"(?:\s(\d+))+" " 1 2 3")

(map #(Integer/parseInt %) (clojure.string/split (clojure.string/trim " 1 2 3") #" "))

(parse-line "42: \"a\"")
(parse-line "123: 12")
(parse-line "8: 1 2 3")

(parse-line "1: 1 2 3 | 4 5 6")
(parse-line "1: 1 | 6")

(some number? ["a" 3 "b"])

(defn resolve-rule-1 [rule rules]
  (loop [[e & rule-rest] rule result []]
    (if-not e
      (flatten result)
      (recur rule-rest
             (conj result (get rules e e))))))

(if-not (some number? ["a" 12 "b"])
  "done"
  "more")

(get (load-rules) 0)

(defn compile-rules [rules]
  (loop [rule (get rules 0)]
    (Thread/sleep 2500)
    (println rule)
    (if-not (some number? rule)
      rule
      (recur (resolve-rule-1 rule rules)))))

(compile-rules {0 [1 1 1] 1 "a"})

(compile-rules (load-rules))

(defn resolve-rule-2 [rule rules]
  (loop [[e & rule-rest] rule result []]
    (if-not e
      rules
      (if (number? e)
        (concat result (get rules e) rule-rest)
        (recur rule-rest (conj result e))))))

(defn compile-rule [rule-id rules]
  (loop [rule (get rules rule-id)]
    (if-not (some number? rule)
      rule
      (recur (resolve-rule-2 rule rules)))))

(compile-rule 42 (load-rules))

(defn load-rules []
  (util/load-input 2020 19 parse-line #(re-matches #"^\d+:.*" %)))

(load-rules)

(defn load-patterns []
  (util/load-input 2020 19 identity #(re-matches #"[ab]+" %)))

(defn part1 []
  nil)

(defn part2 []
  nil)
