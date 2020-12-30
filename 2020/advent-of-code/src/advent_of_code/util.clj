(ns advent-of-code.util
  (:require [clojure.java.io :as io]))

(defn xor [a b] ;; TODO This should be a macro
  (and (or a b)
       (not= a b)))

(defn count-characters [s c]
  (->> s (filter (partial = c)) count))

(defn load-input
  ([year day]
   (load-input year day identity (complement nil?)))
  ([year day transformer]
   (load-input year day transformer (complement nil?)))
  ([year day transformer filter-pred]
   (->> (str "advent_of_code/" year "/day" day "/input")
       io/resource
       io/reader
       line-seq
       (filter filter-pred)
       (mapv transformer))))

(defn load-test-input
  ([year day]
   (load-test-input year day identity (complement nil?)))
  ([year day transformer]
   (load-test-input year day transformer (complement nil?)))
  ([year day transformer filter-pred]
   (->> (str "advent_of_code/" year "/day" day "/test")
       io/resource
       io/reader
       line-seq
       (filter filter-pred)
       (mapv transformer))))

;; (mapv transformer
;;   (filter filter-pred
;;     (doall (line-seq (io/reader (io/resource (str "advent_of_code/" year "/day" day "/input")))))))))

(defn load-input-string
  ([year day]
   (load-input-string year day identity))
  ([year day transformer]
   (transformer (slurp (io/resource (str "advent_of_code/" year "/day" day "/input"))))))

