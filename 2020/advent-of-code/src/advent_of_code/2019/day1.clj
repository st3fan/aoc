(ns advent-of-code.2019.day1
  (:require [advent-of-code.util :as util]))

(defn load-input []
  (util/load-input 2019 1 #(Integer/parseInt %)))

(defn fuel-required [m]
  (- (quot m 3) 2))

(defn part1 []
  (apply + (map fuel-required (load-input))))

(defn fuel-required-2 [m]
  (loop [m (fuel-required m) t m]
    (if (< m 6)
      t
      (let [required (fuel-required m)]
        (recur required (+ t required))))))

(defn part2 []
  (apply + (map fuel-required-2 (load-input))))
