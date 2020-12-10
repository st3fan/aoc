(ns advent-of-code.2015.7
  (:require [advent-of-code.util :as util]
            [clojure.set]))

(defn left-pad [s n c]
  (apply str (concat (take (- n (count s)) (repeat c)) s)))

(defn parse-operation [op]
  (if-let [m (re-matches #"(\d+)" op)]
    ["CONST" (Short/parseShort (nth m 1))]
    (if-let [m (re-matches #"(\w+)" op)]
      ["VAR" (keyword (nth m 1))]
      (if-let [m (re-matches #"(\w+) (LSHIFT|RSHIFT) (\d+)" op)]
        [(nth m 2) (keyword (nth m 1)) (Short/parseShort (nth m 3))]
        (if-let [m (re-matches #"(\d+) (OR|AND) (\w+)" op)]
          [(str (nth m 2) "-CONST") (Short/parseShort (nth m 1)) (keyword (nth m 3))]
          (if-let [m (re-matches #"(\w+) (OR|AND) (\w+)" op)]
            [(nth m 2) (keyword (nth m 1)) (keyword (nth m 3))]
            (if-let [m (re-matches #"NOT (\w+)" op)]
              ["NOT" (keyword (nth m 1))])))))))

(defn parse-line [line]
  (if-let [[_ operation destination] (re-matches #"(.+) -> (\w+)" line)]
    (if-let [operation (parse-operation operation)]
      [(keyword destination) operation])))

(defn load-input []
  (sort-by #(left-pad (str (first %)) 5 " ") (util/load-input 2015 7 parse-line)))

(defn test-input []
  (map parse-line ["123 -> x" "456 -> y" "x AND y -> d" "x OR y -> e" "x LSHIFT 2 -> f" "y RSHIFT 2 -> g" "NOT x -> h" "NOT y -> i"]))

(defn constant-rules [rules]
  (let [constants (filter #(= "CONST" (first (second %))) rules)]
    (into {} (map #(vector (first %) (second (second %))) constants))))

(defn create-circuit [rules]
  {:rules rules
   :variables (constant-rules rules)})

(defn variables-in-rule [[var expression]]
  (set (filter keyword? expression)))

(defn unsolved-rules-with-known-variables [circuit]
  (let [known-variables (set (keys (:variables circuit)))]
    (let [rules (filter #(clojure.set/subset? (set (variables-in-rule %)) known-variables) (:rules circuit))]
      (filter #(not= "CONST" (first (second %))) rules))))

(defn solved? [circuit]
  (= (count (:rules circuit)) (count (:variables circuit))))

(defn solve-expression [variables [op a b]]
  (condp = op
    "CONST"     a
    "VAR"       (get variables a)
    "LSHIFT"    (bit-shift-left (a variables) b)
    "RSHIFT"    (bit-shift-right (a variables) b)
    "OR"        (bit-or (a variables) (b variables))
    "AND"       (bit-and (a variables) (b variables))
    "AND-CONST" (bit-and a (b variables))
    "NOT"       (bit-xor (a variables) 0xffff)))

(defn solve-rules [circuit rules]
  (loop [rules rules variables (:variables circuit)]
    (if (empty? rules)
      variables
      (let [[variable expression] (first rules)]
        (recur (rest rules)
               (assoc variables variable (solve-expression (:variables circuit) expression)))))))

(defn solve [circuit]
  (loop [circuit circuit]
    (if (solved? circuit)
      circuit
      (let [rules-to-solve (unsolved-rules-with-known-variables circuit)
            new-variables (solve-rules circuit rules-to-solve)]
        (recur (update circuit :variables merge new-variables))))))

;;

(defn part1 []
  (-> (load-input) (create-circuit) (solve) :variables :a))

;;

(defn set-signal [circuit signal value]
  (assoc-in circuit [:variables signal] value))

(defn part2 []
  (-> (load-input) (create-circuit) (set-signal :b 46065) (solve) :variables :a))
