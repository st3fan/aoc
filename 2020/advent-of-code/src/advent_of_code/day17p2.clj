(ns advent-of-code.day17p2
  (:require [advent-of-code.util :as util]
            [clojure.math.combinatorics :as combo]))

(defn load-data []
  (let [input (util/load-input 2020 17)]
    (into {} (apply concat (for [[y line] (zipmap (range) input)]
                             (for [[x c] (zipmap (range) line) :when (= c \#)]
                               [{:x x :y y :z 0 :w 0} true]))))))

(defn empty-space []
  (into {} (map #(vector {:x (nth % 0) :y (nth % 1) :z (nth % 2) :w (nth % 3)} false)
                (combo/cartesian-product
                 (range -15 15)
                 (range -15 15)
                 (range -15 15)
                 (range -15 15)))))

(defn build-space []
  (merge (empty-space) (load-data)))

(defn offset-point [p offset]
  {:x (+ (:x p) (nth offset 0))
   :y (+ (:y p) (nth offset 1))
   :z (+ (:z p) (nth offset 2))
   :w (+ (:w p) (nth offset 3))})

(def offsets-around-point
  (filter #(not= [0 0 0 0] %) (combo/cartesian-product [-1 0 1] [-1 0 1] [-1 -0 1] [-1 0 1])))

(defn count-active-neighbours [space p]
  (let [offsets offsets-around-point]
    (loop [[offset & rest-offsets] offsets results []]
      (if (nil? offset)
        (count results)
        (let [p (offset-point p offset) v (get space p)]
          (if (true? v)
            (recur rest-offsets (conj results v))
            (recur rest-offsets results)))))))

(def space (build-space))

(defn count-active-cubes [space]
  (count (filter true? (vals space))))

(defn cycle [space]
  (loop [[[p v] & space-rest] space updated-space space]
    (if (nil? p)
      updated-space
      (let [n (count-active-neighbours space p)]
        (condp = v
          true  (if (or (= n 2) (= n 3))
                  (recur space-rest updated-space)
                  (recur space-rest (assoc updated-space p false)))
          false (if (= n 3)
                  (recur space-rest (assoc updated-space p true))
                  (recur space-rest updated-space))
          :else (recur space-rest updated-space))))))

;; (time (count-active-cubes (cycle space)))

;; (time (-> (build-space)
;;     (cycle)
;;     (cycle)
;;     (cycle)
;;     (cycle)
;;     (cycle)
;;     (cycle)
;;     (count-active-cubes)))

(defn part2 []
  (-> (build-space)
    (cycle)
    (cycle)
    (cycle)
    (cycle)
    (cycle)
    (cycle)
    (count-active-cubes)))
