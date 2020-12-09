(ns advent-of-code.day7
  (:require [clojure.set]
            [clojure.walk :as w]
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

;; Trying

(def test-bags
  {"light red"    {"bright white" 1 "muted yellow" 2}
   "dark orange"  {"bright white" 3 "muted yellow" 4}
   "bright white" {"shiny gold" 1}
   "muted yellow" {"shiny gold" 2 "faded blue" 9}
   "shiny gold"   {"dark olive" 1 "vibrant plum" 2}
   "dark olive"   {"faded blue" 3 "dotted black" 4}
   "vibrant plum" {"faded blue" 5 "dotted black" 6}
   "poop green"   {"faded blue" 5}
   "faded blue"   {}
   "dotted black" {}})

(def test-bags
  [[{:color "light red"}    {:color "bright white" :count 1}]
   [{:color "light red"}    {:color "muted yellow" :count 2}]
   [{:color "dark orange"}  {:color "bright white" :count 3}]
   [{:color "dark orange"}  {:color "muted yellow" :count 4}]
   [{:color "bright white"} {:color "shiny gold"   :count 1}]
   [{:color "muted yellow"} {:color "shiny gold"   :count 2}]
   [{:color "muted yellow"} {:color "faded blue"   :count 9}]
   [{:color "shiny gold"}   {:color "dark olive"   :count 1}]
   [{:color "shiny gold"}   {:color "vibrant plum" :count 2}]
   [{:color "dark olive"}   {:color "faded blue"   :count 3}]
   [{:color "dark olive"}   {:color "dotted black" :count 4}]
   [{:color "vibrant plum"} {:color "faded blue"   :count 5}]
   [{:color "vibrant plum"} {:color "dotted black" :count 6}]
   [{:color "poop green"}   {:color "faded blue"   :count 5}]])

(def test-bags
  [["light red"    "bright white"]
   ["light red"    "muted yellow"]
   ["dark orange"  "bright white"]
   ["dark orange"  "muted yellow"]
   ["bright white" "shiny gold"]
   ["muted yellow" "shiny gold"]
   ["muted yellow" "faded blue"]
   ["shiny gold"   "dark olive"]
   ["shiny gold"   "vibrant plum"]
   ["dark olive"   "faded blue"]
   ["dark olive"   "dotted black"]
   ["vibrant plum" "faded blue"]
   ["vibrant plum" "dotted black"]
   ["poop green"   "faded blue"]
   ;;["faded blue"   nil]
   ;;["dotted black" nil]
   ])

(defn descendants [adj-list node]
  (map second (filter #(= (:color (first %)) (:color node)) adj-list)))

(descendants test-bags {:color "shiny gold"})

(defn ->branch [id kids]
  (merge id {:kids (if (empty? kids) nil kids)}))

(defn ->leaf [id]
  {:id id})

(defn ->tree [adj-list node]
  (let [->tree' (partial ->tree adj-list)]
    (if-let [kid-ids (descendants adj-list node)]
      (->branch node (map ->tree' kid-ids))
      (->leaf node))))

(let [tree (->tree test-bags {:color "shiny gold"})]
  (tree-seq true? :kids tree))


(defn bags-in-bag [bags color]
  (let [bag (get bags color)]
    (apply + (vals bag))))

(defn bags-in-bags [bags colors]
  (reduce + (map #(bags-in-bag bags %) colors)))

(defn count-bags-1 [bags colors acc]
  (if (empty? colors)
    acc
    (let [acc (+ acc (reduce + (map #(bags-in-bag bags %) colors)))]
      (apply + (map #(count-bags-1 bags (keys (get bags %)) acc) colors)))))

;;(foo test-bags ["dark olive" "vibrant plum"] 0)

;; Failing

(defn count-bags-inside-bag [bags bag-color]
  (count-bags-1 bags [bag-color] 0))

(count-bags-inside-bag test-bags "vibrant plum")

(defn part2 []
  (count-bags-inside-bag (load-bags) "shiny gold"))

;;

;; (if-let [matches (re-matches #"(\w+ \w+) bags contain( (\d+) (\w+ \w+) bag(?:, (\d+) (\w+ \w+) bags?)*)?" line)]

;; (re-matches #"" "light red bags contain 1 bright")

;; (re-seq
;;  #"(\d+) (\w+ \w+)"
;;  "light red bags contain 1 bright white bag, 2 muted yellow bags")

;; (parse-line "light red bags contain 1 bright white bag, 2 muted yellow bags")
;; (parse-line "drab white bags contain 1 dotted aqua bag")
;; (parse-line "dim salmon bags contain no other bags")

;; (defn count-bag-color [colors]
;;   ...)

;; (count (filter #(= "green" %) ["blue" "red"]))

;; Return a map of color -> [colors]
;; (defn parse-bags []
;;   ...)

;; (count-bag-color test-bags "shiny gold" (keys test-bags) 0)

;; (let [bags (parse-bags ...)
;;       root-colors (root-bags bags)]
;;   (count-bag-color bags "shiny gold" root-colors))

;; (defn parse-line [line]
;;   (if-let [matches (re-find #"^(\w+ \w+)" line)]
;;     (let [color (nth matches 1)]
;;       (if-let [matches (re-seq #"(\d+) (\w+ \w+)" line)]
;;         {color (mapv #(nth % 2) matches)}
;;         {color []}))))

;; (defn load-bags []
;;   (apply merge (util/load-input 2020 7 parse-line)))

;; (defn count-bag-color [bags search-color colors acc]
;;   (if (empty? colors)
;;     acc
;;     (let [acc (+ acc (count (filter #(= % search-color) colors)))]
;;       (apply + (map #(count-bag-color bags search-color (get bags %) acc) colors)))))

;; (defn part1 []
;;   (let [bags (load-bags)]
;;     (dec (count (filter #(not (zero? (nth % 1))) (map #(vector % (count-bag-color bags "shiny gold" [%] 0)) (keys bags)))))))

;; (defn part2 []
;;   nil)
