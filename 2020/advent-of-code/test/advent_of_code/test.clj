(ns advent-of-code.test
  (:require [clojure.test :refer :all]
            [advent-of-code.2019.day12]
            [advent-of-code.day1 :as day1]
            [advent-of-code.day2 :as day2]
            [advent-of-code.day3 :as day3]
            [advent-of-code.day4 :as day4]))

;; 2019

(deftest year-2019-day-12-test
  (testing "Year 2019, Day 12, Part 1"
    (is (= 10635 (advent-of-code.2019.day12/part1))))
  (testing "Year 2019, Day 12, Part 2"
    (is (= 583523031727256 (advent-of-code.2019.day12/part2)))))

;; 2020

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

(deftest day3-test
  (testing "Day 3, Part 1"
    (is (= 262 (day3/part1))))
  (testing "Day 3, Part 2"
    (is (= 2698900776 (day3/part2)))))

(deftest day4-test
  (testing "Day 4, Part 1"
    (is (= 247 (day4/part1))))
  (testing "Day 4, Part 2"
    (is (= 145 (day4/part2)))))
