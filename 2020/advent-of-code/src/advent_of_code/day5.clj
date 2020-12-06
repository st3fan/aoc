(ns advent-of-code.day5
  (:require [advent-of-code.util :as util]))

(defn seat->row [seat]
  (loop [regions (subs seat 0 7) rows (range 128)]
    (if (= 1 (count rows))
      (first rows)
      (case (first regions)
        \F (recur (rest regions) (first  (split-at (quot (count rows) 2) rows)))
        \B (recur (rest regions) (second (split-at (quot (count rows) 2) rows)))))))

(defn seat->column [seat]
  (loop [regions (subs seat 7) rows (range 8)]
    (if (= 1 (count rows))
      (first rows)
      (case (first regions)
        \L (recur (rest regions) (first  (split-at (quot (count rows) 2) rows)))
        \R (recur (rest regions) (second (split-at (quot (count rows) 2) rows)))))))

(defn seat->id [seat]
  (+ (* 8 (seat->row seat)) (seat->column seat)))

(defn part1 []
  (apply max (map seat->id (util/load-input 2020 5))))

;;

(defn seat-test [taken row column min-row max-row]
  (and (not (contains? taken [row column]))
       (> row min-row)
       (< row max-row)))

(defn part2 []
  (let [input (util/load-input 2020 5)
        taken (set (map #(vector (seat->row %) (seat->column %)) (util/load-input 2020 5)))
        min-row (apply min (map seat->row input))
        max-row (apply max (map seat->row input))]
    (first (for [row (range 128) column (range 8) :when (seat-test taken row column min-row max-row)]
      (+ (* 8 row) column)))))

;; (defn decode [code]
;;   (-> (clojure.string/escape code {\F 0 \L 0 \B 1 \R 1})
;;       (Long/parseLong 2)))
