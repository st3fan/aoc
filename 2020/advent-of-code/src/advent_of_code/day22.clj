(ns advent-of-code.day22)

(def starting-deck1 [19 22 43 38 23 21 2 40 31 17 27 28 35 44 41 47 50 7 39 5 42 25 33 3 48])

(def starting-deck2 [16 24 36 6 34 11 8 30 26 15 9 10 14 1 12 4 32 13 18 46 37 29 20 45 49])

(defn score-deck [deck]
  (reduce + (map-indexed #(* (inc %1) %2) (reverse deck))))

(defn declare-winner [deck1 deck2]
  (if (empty? deck2)
    {:player 1 :score (score-deck deck1) :deck deck1}
    {:player 2 :score (score-deck deck2) :deck deck2}))

(defn simple-crabs [deck1 deck2]
  (loop [deck1 deck1 deck2 deck2]
    (if (or (empty? deck1) (empty? deck2))
      (declare-winner deck1 deck2)
      (let [card1 (first deck1) card2 (first deck2)]
        (if (> card1 card2)
          (recur (conj (subvec deck1 1) card1 card2)
                 (subvec deck2 1))
          (recur (subvec deck1 1)
                 (conj (subvec deck2 1) card2 card1)))))))

(defn part1 []
  (simple-crabs starting-deck1 starting-deck2))

;;

(defn recursive-crabs [deck1 deck2]
  (loop [deck1 deck1 deck2 deck2 previous-decks #{}]
    (if (or (empty? deck1) (empty? deck2))
      (declare-winner deck1 deck2)
      (if (or (contains? previous-decks deck1) (contains? previous-decks deck2))
        {:player 1 :reason :deck-seen-before :score (score-deck deck1)}
        (let [card1 (first deck1) card2 (first deck2)]
          (if (and (> (count deck1) card1) (> (count deck2) card2))
            (let [winner (recursive-crabs (subvec deck1 1 (inc card1)) (subvec deck2 1 (inc card2)))]
              (if (= 1 (:player winner))
                (recur (conj (subvec deck1 1) card1 card2)
                       (subvec deck2 1)
                       (conj previous-decks deck1 deck2))
                (recur (subvec deck1 1)
                       (conj (subvec deck2 1) card2 card1)
                       (conj previous-decks deck1 deck2))))
            (if (> card1 card2)
              (recur (conj (subvec deck1 1) card1 card2)
                     (subvec deck2 1)
                     (conj previous-decks deck1 deck2))
              (recur (subvec deck1 1)
                     (conj (subvec deck2 1) card2 card1)
                     (conj previous-decks deck1 deck2)))))))))

(defn part2 []
  (recursive-crabs starting-deck1 starting-deck2))

