(ns advent-of-code.day23)

(defn init-game [labels]
  {:cups labels
   :current (first labels)
   :removed nil})

;; The crab picks up the three cups that are immediately clockwise of
;; the current cup. They are removed from the circle; cup spacing is
;; adjusted as necessary to maintain the circle.

(defn remove-cups [game]
  (loop [cups (:cups game) index (.indexOf (:cups game) (:current game)) removed []]
    (if (= 3 (count removed))
      (merge game {:cups (vec (filter number? cups)) :removed removed})
      (let [index (mod (inc index) (count (:cups game))) value (get cups index)]
        (recur (assoc cups index nil) index (conj removed value))))))

(remove-cups {:cups [3  2 5 4  6  7  8  9  1] :current 5 :removed nil})

(defn insert-cups [game cups]
  game)

(defn next-current [game]
  (update game :current #(mod (inc %) (count (:cups game)))))

(defn move [game]
  (-> game
      (remove-cups)))

;; The crab selects a destination cup: the cup with a label equal to
;; the current cup's label minus one. If this would select one of the
;; cups that was just picked up, the crab will keep subtracting one
;; until it finds a cup that wasn't just picked up. If at any point in
;; this process the value goes below the lowest value on any cup's
;; label, it wraps around to the highest value on any cup's label
;; instead.

(defn destination-cup [game]
  (let [lowest (apply min (filter number? (:cups game)))]
    (loop [index (mod (inc (:current game)) (count (:cups game)))]
      (let [value (nth (:cups game) index)]
        (if (< value lowest)
          (apply max (filter number? (:cups game)))

          (if (not= -1 (.indexOf (:cups game) value))
            (.indexOf (:cups game) value)

            (recur (dec value))))))))

(defn destination-cup [current cups]
  (let [lowest (apply min cups) cups (set cups)]
    (loop [current (dec current)]
      (if (< current lowest)
        (apply max cups)
        (if-let [v (get cups current)]
          v
          (recur (dec current)))))))

(destination-cup 3 [8 9 5 4 6 7])

(destination-cup (remove-cups (init-game [3 8 9 1 2 5 4 6 7])))

(remove-cups {:cups [3  2 5 4  6  7  8  9  1] :current 5 :removed nil})

(destination-cup 5 [3 2 5 8 9 1]) ;; 3

(defn insert-cups [dst cups new]
  (let [index (.indexOf cups dst)]
    (let [[before after] (split-at (inc index) cups)]
      (vec (concat before new after)))))



(insert-cups 4 [1 2 4 3] [7 8 9])

(insert-cups 3 [3 2 5 8 9 1] [4 6 7])


(defn move [game]
  (let [game (remove-cups game)]
    (let [dst (destination-cup (:current game) (:cups game))]
      {:current dst
       :cups (insert-cups dst (:cups game) (:removed game))
       :removed nil})))

(insert-removed-cups (remove-cups (init-game [3 8 9 1 2 5 4 6 7])))


(move (init-game [3 8 9 1 2 5 4 6 7]))

(insert-cups 2 [3 2 5 4 6 7] [8 9 1])

(take-nth 2 (iterate move (init-game [3 8 9 1 2 5 4 6 7])))

(let [game (init-game [3 8 9 1 2 5 4 6 7])]
  (loop [n 10 game game]
    (when-not (zero? n)
      (println game)
      (recur (dec n) (move game)))))












(defn init-game [labels]
  {:cups labels
   :current (first labels)
   :removed nil})

(defn remove-cups [game]
  (loop [cups (:cups game) index (.indexOf (:cups game) (:current game)) removed []]
    (if (= 3 (count removed))
      (merge game {:cups (vec (filter number? cups)) :removed removed})
      (let [index (mod (inc index) (count (:cups game))) value (get cups index)]
        (recur (assoc cups index nil) index (conj removed value))))))

(defn get-destination [game]
  (let [lowest (apply min (:cups game)) cups (set (:cups game))]
    (loop [current (dec (:current game))]
      (if (< current lowest)
        (apply max cups)
        (if-let [v (get cups current)]
          v
          (recur (dec current)))))))

(defn insert-removed-cups [game]
  (let [destination (get-destination game)]
    (let [index (.indexOf (:cups game) destination)]

      ;;(let [[before after] (split-at (inc index) (:cups game))]
      ;;  {:cups (vec (concat before (:removed game) after))

      (let [before (subvec (:cups game) 0 index) after (subvec (:cups game) index)]
        {:cups (into (into before (:removed game)) after)


         :current (:current game)
         :removed nil}))))

;; The crab selects a new current cup: the cup which is immediately
;; clockwise of the current cup.

(defn update-current [game]
  (let [index (.indexOf (:cups game) (:current game))]
    (let [new-index (mod (inc index) (count (:cups game)))]
      (assoc game :current (get (:cups game) new-index)))))

(defn move [game]
  (-> game
      (remove-cups)
      (insert-removed-cups)
      (update-current)))

(defn answer [game]
  (let [index (.indexOf (:cups game) 1)]
    (let [[before after] (split-at (inc index) (:cups game))]
      (Integer/parseInt (apply str (concat after before))))))

(defn part1 []
  (let [game (nth (iterate move (init-game [4 1 8 9 7 6 2 3 5])) 100)]
    (answer game))) ;; 963428751

(defn answer2 [game]
  (let [index (.indexOf (:cups game) 1)]
    (* (get (:cups game) (+ index 1)) (get (:cups game) (+ index 2)))))

(defn part2 []
  (let [labels (vec (concat [4 1 8 9 7 6 2 3 5] (range 10 1000001)))]
    (let [game (nth (iterate move (init-game labels)) 1000)]
      (answer2 game))))
