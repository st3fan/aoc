(ns advent-of-code.day14
  (:require [advent-of-code.util :as util]
            [clojure.string :as string]))

(defn parse-mask [s]
  [(Long/parseLong (-> s (string/replace #"0" "T") (string/replace #"[1X]" "1") (string/replace #"T" "0")) 2)
   (Long/parseLong (-> s (string/replace #"1" "T") (string/replace #"[1X]" "0") (string/replace #"T" "1")) 2)])

(defn parse-line [line]
  (if-let [matches (re-matches #"mask = ([X10]{36})" line)]
    [:mask (parse-mask (nth matches 1))]
    (if-let [matches (re-matches #"mem\[(\d+)\] = (\d+)" line)]
      [:mem (Long/parseLong (nth matches 1)) (Long/parseLong (nth matches 2))])))

(defn load-input []
  (util/load-input 2020 14 parse-line))

(defn apply-mask [[zero-mask one-mask] value]
  (-> value (bit-and zero-mask) (bit-or one-mask)))

(defn process-program [program]
  (loop [[instruction & instructions] program memory {} current-mask nil]
    (if-not instruction
      memory
      (let [[op a b] instruction]
        (condp = op
          :mem  (recur instructions
                       (assoc memory a (apply-mask current-mask b))
                       current-mask)
          :mask (recur instructions
                       memory
                       a))))))

(defn part1 []
  (apply + (vals (process-program (load-input)))))
