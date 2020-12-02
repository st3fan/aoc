(ns advent-of-code.test
  (:require [clojure.test :refer :all]
            [advent-of-code.day2 :as day2]))

(deftest day2-test
  (testing "Day 2, Part 1"
    (is (= 638 (day2/part1))))
  (testing "Day 2, Part 2"
    (is (= 699 (day2/part2)))))
