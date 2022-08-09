(ns sonar-sweep.core-test
  (:require [clojure.test :refer :all]
            [sonar-sweep.core :refer :all]))

(deftest sonar-sweep-test
  (testing "Sonar Sweep - Part 1"
    (is (= (part1) 1532)))
  (testing "Sonar Sweet - Part 2"
    (is (= (part2) 1571))))
