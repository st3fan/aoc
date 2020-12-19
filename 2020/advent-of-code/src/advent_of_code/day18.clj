(ns advent-of-code.day18
  (:require [advent-of-code.util :as util]
            [instaparse.core :as insta]))

(defn parse-line [line]
  (clojure.string/replace line #" " ""))

(def arithmetic1
  (insta/parser
    "expr   = term | add | mul
     add    = expr <'+'> term
     mul    = expr <'*'> term
     <term> = number | <'('> expr <')'>
     number = #'[0-9]+'"))

(defn evaluate-expression1 [e]
  (->> (arithmetic1 e)
       (insta/transform {:add + :mul * :number clojure.edn/read-string :expr identity})))

(defn part1 []
  (let [expressions (util/load-input 2020 18 parse-line)]
    (reduce + (map evaluate-expression1 expressions))))

;;

(def arithmetic2
  (insta/parser
    "expr      = mul-add | mul
     mul       = expr <'*'> mul-add
     <mul-add> = term | add
     add       = mul-add <'+'> term
     <term>    = number | <'('> expr <')'>
     number    = #'[0-9]+'"))

(defn evaluate-expression2 [e]
  (->> (arithmetic2 e)
       (insta/transform {:add + :mul * :number clojure.edn/read-string :expr identity})))

(defn part2 []
  (let [expressions (util/load-input 2020 18 parse-line)]
    (reduce + (map evaluate-expression2 expressions))))
