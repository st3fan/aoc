(ns advent-of-code.2019.day5
  (:require [advent-of-code.util :as util]
            [clojure.math.combinatorics :as combo]))

(defn create-int-computer [program input]
  {:input input
   :output []
   :memory program
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

(defn first-input [computer]
  (first (:input computer)))

(defn pop-input [computer]
  (assoc computer :input (rest (:input computer))))

(defn push-output [computer value]
  (assoc computer :output (conj (:output computer) value)))

(def ADD     1)
(def MUL     2)
(def INPUT   3)
(def OUTPUT  4)
(def HALT   99)

(defn execute [int-computer]
  (loop [ic int-computer]
    (condp = (current-instruction ic)
      ADD    (let [a (first-arg ic) b (second-arg ic) dst (third-arg ic)]
               (let [ic (set-memory ic dst (+ (get-memory ic a) (get-memory ic b)))]
                 (recur (increment-pc ic 4))))
      MUL    (let [a (first-arg ic) b (second-arg ic) dst (third-arg ic)]
               (let [ic (set-memory ic dst (* (get-memory ic a) (get-memory ic b)))]
                 (recur (increment-pc ic 4))))
      INPUT  (let [dst (first-arg ic) value (first-input ic)]
               (let [ic (set-memory ic dst value)]
                 (let [ic (pop-input ic)]
                   (recur (increment-pc ic 2)))))
      OUTPUT (let [src (first-arg ic) value (get-memory ic src)]
               (let [ic (push-output ic value)]
                 (recur (increment-pc ic 2))))
      HALT   ic)))

(def program [3 0 4 0 99])

(defn run-program [program]
  (-> (create-int-computer program [42])
      (execute)
      :output))

(run-program program)

(defn part1 []
  (run-program program 12 2))

(defn calculate-answer [[a b]]
  (+ (* 100 a) b))

(defn part2 []
  (->> (combo/permuted-combinations (range 100) 2)
       (filter #(= 19690720 (run-program program (first %) (second %))))
       (first)
       (calculate-answer)))
