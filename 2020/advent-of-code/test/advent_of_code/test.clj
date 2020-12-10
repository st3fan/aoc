(ns advent-of-code.test
  (:require [clojure.test :refer :all]
            [advent-of-code.2015.1]
            [advent-of-code.2015.2]
            [advent-of-code.2015.3]
            [advent-of-code.2015.4]
            [advent-of-code.2015.5]
            [advent-of-code.2015.6]
            [advent-of-code.2019.day2]
            [advent-of-code.2019.day12]
            [advent-of-code.day1 :as day1]
            [advent-of-code.day2 :as day2]
            [advent-of-code.day3 :as day3]
            [advent-of-code.day4 :as day4]
            [advent-of-code.day5 :as day5]
            [advent-of-code.day6 :as day6]
            [advent-of-code.day7 :as day7]
            [advent-of-code.day8 :as day8]
            [advent-of-code.day9 :as day9]))

;; 2015

(deftest year-2015-day-1-test
  (testing "Year 2015, Day 1, Part 1"
    (is (=  280 (advent-of-code.2015.1/part1))))
  (testing "Year 2015, Day 1, Part 2"
    (is (= 1797 (advent-of-code.2015.1/part2)))))

(deftest year-2015-day-2-test
  (testing "Year 2015, Day 2, Part 1"
    (is (= 1588178 (advent-of-code.2015.2/part1))))
  (testing "Year 2015, Day 2, Part 2"
    (is (= 3783758 (advent-of-code.2015.2/part2)))))

(deftest year-2015-day-3-test
  (testing "Year 2015, Day 3, Part 1"
    (is (= 2572 (advent-of-code.2015.3/part1))))
  (testing "Year 2015, Day 3, Part 2"
    (is (= 2631 (advent-of-code.2015.3/part2)))))

(deftest year-2015-day-4-test
  (testing "Year 2015, Day 4, Part 1"
    (is (=  254575 (advent-of-code.2015.4/part1))))
  (testing "Year 2015, Day 4, Part 2"
    (is (= 1038736 (advent-of-code.2015.4/part2)))))

(deftest year-2015-day-5-test
  (testing "Year 2015, Day 5, Part 1"
    (is (= 238 (advent-of-code.2015.5/part1))))
  (testing "Year 2015, Day 5, Part 2"
    (is (=  69 (advent-of-code.2015.5/part2)))))

(deftest year-2015-day-6-test
  (testing "Year 2015, Day 6, Part 1"
    (is (= 543903 (advent-of-code.2015.6/part1))))
  (testing "Year 2015, Day 6, Part 2"
    (is (= 14687245 (advent-of-code.2015.6/part2)))))

;; 2019

(deftest year-2019-day-2-test
  (testing "Year 2019, Day 2, Part 1"
    (is (= 2692315 (advent-of-code.2019.day2/part1))))
  (testing "Year 2019, Day 2, Part 2"
    (is (= 9507 (advent-of-code.2019.day2/part2)))))

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

(deftest day5-test
  (testing "Day 5, Part 1"
    (is (= 989 (day5/part1))))
  (testing "Day 5, Part 2"
    (is (= 548 (day5/part2)))))

(deftest day6-test
  (testing "Day 6, Part 1"
    (is (= 6587 (day6/part1))))
  (testing "Day 6, Part 2"
    (is (= 3235 (day6/part2)))))

(deftest day7-test
  (testing "Day 7, Part 1"
    (is (= 242 (day7/part1))))
  (testing "Day 7, Part 2"
    (is (= 176035 (day7/part2)))))

(deftest day8-test
  (testing "Day 8, Part 1"
    (is (= 1709 (day8/part1))))
  (testing "Day 6, Part 2"
    (is (= 1976 (day8/part2)))))

(deftest day9-test
  (testing "Day 9, Part 1"
    (is (= 177777905 (day9/part1))))
  (testing "Day 9, Part 2"
    (is (= 23463012 (day9/part2)))))
