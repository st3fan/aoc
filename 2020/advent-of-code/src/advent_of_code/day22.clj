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
      ;; Game ends when one of the decks is empty
      (declare-winner deck1 deck2)
      ;; Play a round
      (let [card1 (first deck1) card2 (first deck2)]
        (if (> card1 card2)
          ;; Player 1 wins
          (recur (conj (subvec deck1 1) card1 card2)
                 (subvec deck2 1))
          ;; Player 2 wins
          (recur (subvec deck1 1)
                 (conj (subvec deck2 1) card2 card1)))))))

(defn part1 []
  (simple-crabs starting-deck1 starting-deck2))

;;

(defn recursive-crabs [deck1 deck2]
  (loop [deck1 deck1 deck2 deck2 previous-decks #{}]
    (if (or (empty? deck1) (empty? deck2))
      ;; Game ends when one of the decks is empty
      (declare-winner deck1 deck2)
      ;; If there was a previous round in this game that had exactly the
      ;; same cards in the same order in the same players' decks, the
      ;; game instantly ends in a win for player 1
      (if (or (contains? previous-decks deck1) (contains? previous-decks deck2))
        {:player 1 :reason :deck-seen-before :score (score-deck deck1)}
        ;; Otherwise, this round's cards must be in a new configuration;
        ;; the players begin the round by each drawing the top card of
        ;; their deck as normal.
        (let [card1 (first deck1) card2 (first deck2)]
          ;; If both players have at least as many cards remaining in
          ;; their deck as the value of the card they just drew ...
          (if (and (> (count deck1) card1) (> (count deck2) card2))
            ;; ... the winner of the round is determined by playing a
            ;; new game of Recursive Combat. To play a sub-game of
            ;; Recursive Combat, each player creates a new deck by
            ;; making a copy of the next cards in their deck (the
            ;; quantity of cards copied is equal to the number on the
            ;; card they drew to trigger the sub-game).
            (let [winner (recursive-crabs (subvec deck1 1 (inc card1)) (subvec deck2 1 (inc card2)))]
              (if (= 1 (:player winner))
                (recur (conj (subvec deck1 1) card1 card2)
                       (subvec deck2 1)
                       (conj previous-decks deck1 deck2))
                (recur (subvec deck1 1)
                       (conj (subvec deck2 1) card2 card1)
                       (conj previous-decks deck1 deck2))))
            ;; Otherwise, at least one player must not have enough cards
            ;; left in their deck to recurse; the winner of the round is
            ;; the player with the higher-value card.
            (if (> card1 card2)
              (recur (conj (subvec deck1 1) card1 card2)
                     (subvec deck2 1)
                     (conj previous-decks deck1 deck2))
              (recur (subvec deck1 1)
                     (conj (subvec deck2 1) card2 card1)
                     (conj previous-decks deck1 deck2)))))))))

(defn part2 []
  (recursive-crabs starting-deck1 starting-deck2))

