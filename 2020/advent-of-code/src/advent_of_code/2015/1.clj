(ns advent-of-code.2015.1
  (:require [advent-of-code.util :as util]))

(defn part1 []
  (let [input (util/load-input-string 2015 1) counts (frequencies input)]
    (- (get counts \()
       (get counts \)))))

(defn part2 []
  (let [input (util/load-input-string 2015 1)]
    (loop [input input floor 0 position 0]
      (if (neg? floor)
        position
        (recur (rest input)
               (+ floor (if (= (first input) \() 1 -1))
               (inc position))))))
