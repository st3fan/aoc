(ns dive.core-test
  (:require [clojure.test :refer :all]
            [dive.core :refer :all]))

(deftest dive-test
  (testing "Dive - Part 1"
    (is (= (part1) 1855814)))
  (testing "Dive - Part 2"
    (is (= (part2) 1845455714))))
