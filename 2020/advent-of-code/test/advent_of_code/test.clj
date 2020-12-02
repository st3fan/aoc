(ns advent-of-code.test
  (:require [clojure.test :refer :all]
            [advent-of-code.day1 :as day1]
            [advent-of-code.day2 :as day2]))

(deftest day1-test
  (testing "Day 1, Part 1"
    (is (= 713184 (day1/part1))))
  (testing "Day 1, Part 2"
    (is (= 261244452 (day1/part2)))))

(deftest day2-test
  (testing "Day 2, Part 1"
    (is (= 638 (day2/part1))))
  (testing "Day 2, Part 2"
    (is (= 699 (day2/part2)))))
