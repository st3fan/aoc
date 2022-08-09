(ns giant-squid.core-test
  (:require [clojure.test :refer :all]
            [giant-squid.core :refer :all]))

(deftest giant-squid-test
  (testing "Giant Squid - Part 1"
    (is (= (part1) 0)))
  (testing "Giant Squid - Part 2"
    (is (= (part2) 0))))
