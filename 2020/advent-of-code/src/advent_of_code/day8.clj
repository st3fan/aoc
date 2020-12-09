(ns advent-of-code.day8
  (:require [advent-of-code.util :as util]))

(defn parse-line [line]
  (if-let [matches (re-matches #"(\w+) ([+-]\d+)" line)]
    [(nth matches 1) (Integer/parseInt (nth matches 2)) nil]))

(defn load-program []
  (vec (util/load-input 2020 8 parse-line)))

(defn create-device [program]
  {:memory program
   :pc 0
   :accumulator 0})

(defn current-instruction [device]
  (nth (:memory device) (:pc device)))

(defn increment-pc [device n]
  (let [device (assoc-in device [:memory (:pc device) 2] :seen)]
    (assoc device :pc (+ (:pc device) n))))

(defn set-accumulator [device value]
  (assoc device :accumulator value))

(defn get-accumulator [device]
  (:accumulator device))

(defn pc-at-end [device]
  (= (:pc device) (count (:memory device))))

(defn execute-instructions [device]
  (loop [device device]
    (if (pc-at-end device)
      (assoc device :exit-code :ended)
      (let [[op arg seen] (current-instruction device)]
        (if seen
          (assoc device :exit-code :infinite-loop)
          (condp = (first (current-instruction device))
            "acc"  (let [device (set-accumulator device (+ (get-accumulator device) arg))]
                     (recur (increment-pc device 1)))
            "jmp"  (recur (increment-pc device arg))
            "nop"  (recur (increment-pc device 1))))))))

(defn run-program []
  (-> (create-device (load-program))
      (execute-instructions)
      :accumulator))

;; Run the program and report back on the accumulator

(defn part1 []
  (-> (create-device (load-program))
      (execute-instructions)
      :accumulator))

;; Simple strategy - try to replace them all, report back on the first program that returns normally.

(defn positions-of-jmp-instructions [program]
  (filter #(= "jmp" (first (get program %))) (range (count program))))

(defn patch-instruction [device position]
  (assoc-in device [:memory position 0] "nop"))

;; Patch, run and report back the accumulator if the program ended normally, otherwise nil.
(defn patch-and-run [program position]
  (let [d (-> (create-device program) (patch-instruction position) (execute-instructions))]
    (if (= :ended (:exit-code d))
      (:accumulator d))))

(defn part2 []
  (let [program (load-program) positions (positions-of-jmp-instructions program)]
    (some #(patch-and-run program %) positions)))
