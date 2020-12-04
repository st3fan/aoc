(ns advent-of-code.util
  (:require [clojure.java.io :as io]))

(defn xor [a b] ;; TODO This should be a macro
  (and (or a b)
       (not= a b)))

(defn count-characters [s c]
  (->> s (filter (partial = c)) count))

(defn load-input
  ([year day]
   (load-input year day identity))
  ([year day transformer]
   (map transformer (line-seq (io/reader (io/resource (str "advent_of_code/" year "/day" day "/input")))))))
