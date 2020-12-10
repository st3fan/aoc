(ns advent-of-code.day7
  (:require [clojure.set]
            [clojure.walk :as w]
            [advent-of-code.util :as util]
            [ubergraph.core :as uber]
            [ubergraph.alg :as alg]))

(defn parse-line [line]
  (if-let [matches (re-find #"^(\w+ \w+)" line)]
    (let [color (nth matches 1)]
      (if-let [matches (re-seq #"(\d+) (\w+ \w+)" line)]
        {color (into {} (mapv #(vector (nth % 2) (Integer/parseInt (nth % 1))) matches))}
        {color {}}))))

(defn load-bags []
  (apply merge (util/load-input 2020 7 parse-line)))

;;

(defn part1 []
  (let [g (uber/digraph (load-bags))]
    (dec (count (filter #(alg/shortest-path g % "shiny gold") (uber/nodes g))))))

;;

(defn nested-count [g node]
  (reduce + 1 (map #(* (uber/weight g node %) (nested-count g %)) (uber/successors g node))))

(defn part2 []
  (let [g (uber/digraph (load-bags))]
    (dec (nested-count g "shiny gold"))))
