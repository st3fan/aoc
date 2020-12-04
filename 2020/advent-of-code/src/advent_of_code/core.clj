(ns advent-of-code.core
  (:require [clojure.math.combinatorics :as combo]))

(defn create-int-computer [program]
  {:memory program
   :pc 0})

(defn current-instruction [computer]
  (nth (:memory computer) (:pc computer)))

(defn first-arg [computer]
  (nth (:memory computer) (+ (:pc computer) 1)))

(defn second-arg [computer]
  (nth (:memory computer) (+ (:pc computer) 2)))

(defn third-arg [computer]
  (nth (:memory computer) (+ (:pc computer) 3)))

(defn set-memory [computer address value]
  (assoc-in computer [:memory address] value))

(defn get-memory [computer address]
  (nth (:memory computer) address))

(defn increment-pc [computer n]
  (assoc computer :pc (+ (:pc computer) n)))

(def ADD 1)
(def MUL 2)
(def HALT 99)

(defn execute [int-computer]
  (loop [ic int-computer]
    (condp = (current-instruction ic)
      ADD  (let [a (first-arg ic) b (second-arg ic) dst (third-arg ic)]
               (let [ic (set-memory ic dst (+ (get-memory ic a) (get-memory ic b)))]
                 (recur (increment-pc ic 4))))
      MUL  (let [a (first-arg ic) b (second-arg ic) dst (third-arg ic)]
               (let [ic (set-memory ic dst (* (get-memory ic a) (get-memory ic b)))]
                 (recur (increment-pc ic 4))))
      HALT ic)))

(def program [1 0 0 3 1 1 2 3 1 3 4 3 1 5 0 3 2 1 6 19 1 19 5 23 2 13
              23 27 1 10 27 31 2 6 31 35 1 9 35 39 2 10 39 43 1 43 9
              47 1 47 9 51 2 10 51 55 1 55 9 59 1 59 5 63 1 63 6 67 2
              6 67 71 2 10 71 75 1 75 5 79 1 9 79 83 2 83 10 87 1 87 6
              91 1 13 91 95 2 10 95 99 1 99 6 103 2 13 103 107 1 107 2
              111 1 111 9 0 99 2 14 0 0])

(defn run-program [program a b]
  (-> (create-int-computer program)
      (set-memory 1 a)
      (set-memory 2 b)
      (execute)
      (get-memory 0)))

(defn part1 []
  (run-program program 12 2))

(defn calculate-answer [[a b]]
  (+ (* 100 a) b))

(defn part2 []
  (->> (combo/permuted-combinations (range 100) 2)
       (filter #(= 19690720 (run-program program (first %) (second %))))
       (first)
       (calculate-answer)))
