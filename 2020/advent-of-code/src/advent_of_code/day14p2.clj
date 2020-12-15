(ns advent-of-code.day14p2
  (:require [clojure.math.combinatorics :as combinatorics]
            [clojure.string :as string]
            [advent-of-code.util :as util]))

(defn parse-mask [s]
  [(Long/parseLong (-> s (string/replace #"X" "0")) 2)
   (Long/parseLong (-> s (string/replace #"[01]" "1") (string/replace #"X" "0")) 2)
   (Long/parseLong (-> s (string/replace #"1" "0") (string/replace #"X" "1")) 2)])

(defn parse-line [line]
  (if-let [matches (re-matches #"mask = ([X10]{36})" line)]
    [:mask (parse-mask (nth matches 1))]
    (if-let [matches (re-matches #"mem\[(\d+)\] = (\d+)" line)]
      [:mem (Long/parseLong (nth matches 1)) (Long/parseLong (nth matches 2))])))

(defn load-input []
  (util/load-input 2020 14 parse-line))

(defn bits-set [mask]
  (loop [[n & rest] (range 36) bits []]
    (if-not n
      bits
      (if (bit-test mask n)
        (recur rest (conj bits n))
        (recur rest bits)))))

(defn floating-combinations [floating-mask]
  (conj (set (apply concat (combinatorics/partitions (bits-set floating-mask)))) []))

(defn bits->long [bits]
  (loop [[n & rest] bits r 0]
    (if-not n
      r
      (recur rest (bit-set r n)))))

(defn decode-address [address [set-mask clear-mask floating-mask]]
  (let [address (-> address (bit-or set-mask) (bit-and clear-mask))]
    (loop [[bits & rest] (floating-combinations floating-mask) addresses []]
      (if (nil? bits)
        addresses
        (recur rest
               (conj addresses (bit-or address (bits->long bits))))))))

(defn mem-set [memory addresses value]
  (loop [[address & rest] addresses memory memory]
    (if (nil? address)
      memory
      (recur rest (assoc memory address value)))))

(defn process-program [program]
  (loop [[instruction & instructions] program memory {} current-mask nil]
    (if-not instruction
      memory
      (let [[op a b] instruction]
        (condp = op
          :mem  (recur instructions
                       (mem-set memory (decode-address a current-mask) b)
                       current-mask)
          :mask (recur instructions
                       memory
                       a))))))

(defn part2 []
  (apply + (vals (process-program (load-input)))))
