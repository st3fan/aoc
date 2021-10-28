(ns advent-of-code.day20
  (:require [advent-of-code.util :as util]
            [clojure.math.combinatorics :as combo]
            [clojure.string :as string]))

(defn parse-top [tile-data]
  (seq (first tile-data)))

(defn parse-left [tile-data]
  (map #(first %) tile-data))

(defn parse-bottom [tile-data]
  (seq (last tile-data)))

(defn parse-right [tile-data]
  (map #(last %) tile-data))

(defn parse-tile [chunk]
  (let [[_ number] (re-matches #"Tile (\d+):" (first chunk))]
    {:id (Integer/parseInt number)
     :top (parse-top (rest chunk))
     :left (parse-left (rest chunk))
     :bottom (parse-bottom (rest chunk))
     :right (parse-right (rest chunk))}))

(defn load-tiles []
  (let [lines (util/load-input 2020 20) chunks (take-nth 2 (partition-by empty? lines))]
    (map parse-tile chunks)))

;;

(defn flip-horizontal [tile]
  {:id (:id tile)
   :top (reverse (:top tile))
   :left (:right tile)
   :bottom (reverse (:bottom tile))
   :right (:left tile)})

(defn flip-vertical [tile]
  {:id (:id tile)
   :top (:bottom tile)
   :left (reverse (:left tile))
   :bottom (:top tile)
   :right (reverse (:right tile))})

(defn rotate [tile]
  {:id (:id tile)
   :top (:left tile)
   :left (:bottom tile)
   :bottom (:right tile)
   :right (:top tile)})

(defn all-rotations [tile]
  [tile
   (rotate tile)
   (rotate (rotate tile))
   (rotate (rotate (rotate tile)))])

(defn all-positions [tile]
  (apply concat
         (all-rotations tile)
         (all-rotations (flip-horizontal tile))
         (all-rotations (flip-vertical tile))
         (all-rotations (flip-vertical (flip-horizontal tile)))))

(defn all-possible-edges [tile]
  (let [all (all-positions tile)]
    (apply concat (map #(vector (:top %) (:left %) (:bottom %) (:right %)) all))))

(all-positions (first (load-tiles)))

;;

(defn count-overlap [s1 s2]
  (count (clojure.set/intersection (set s1) (set s2))))

(let [tiles (load-tiles)
      all (map #(all-possible-edges %) tiles)]
  (frequencies (map #(apply count-overlap %) (combo/combinations all 2))))



(let [lines (util/load-input 2020 20) chunks (take-nth 2 (partition-by empty? lines))]
  (count chunks))
