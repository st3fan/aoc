(ns advent-of-code.day6
  (:require [clojure.set]
            [advent-of-code.util :as util]))

(defn parse-line [line]
  (if-let [matches (re-find #"^(\w+ \w+)" line)]
    (let [color (nth matches 1)]
      (if-let [matches (re-seq #"(\d+) (\w+ \w+)" line)]
        {color (into {} (mapv #(vector (nth % 2) (Integer/parseInt (nth % 1))) matches))}
        {color {}}))))

(defn load-bags []
  (apply merge (util/load-input 2020 7 parse-line)))

;; Crappy Code Alert

(defn bags-contains-color-1? [bags search-color colors acc]
  (if (empty? colors)
    acc
    (let [acc (+ acc (count (filter #(= % search-color) colors)))]
      (apply + (map #(bags-contains-color-1? bags search-color (keys (get bags %)) acc) colors)))))

(defn bag-contains-color? [bags search-color bag-color]
  (and (not= search-color bag-color)
       (not (zero? (bags-contains-color-1? bags search-color [bag-color] 0)))))

(defn count-bags-containing-color [bags search-color]
  (count (filter #(bag-contains-color? bags search-color %) (keys bags))))

(defn part1 []
  (count-bags-containing-color (load-bags) "shiny gold"))
