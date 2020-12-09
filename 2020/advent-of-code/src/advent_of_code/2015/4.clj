(ns advent-of-code.2015.4
  (:import java.security.MessageDigest)
  (:require [advent-of-code.util :as util]))

(defn md5 [^String s]
  (let [algorithm (MessageDigest/getInstance "MD5")
        raw (.digest algorithm (.getBytes s))]
    (format "%032x" (BigInteger. 1 raw))))

(defn hash-coin [prefix n]
  (md5 (str prefix n)))

(defn mine [prefix n]
  (let [zeros (apply str (repeat n \0))]
    (filter #(clojure.string/starts-with? (hash-coin prefix %) zeros) (range))))

(defn part1 []
  (first (mine "bgvyzdsv" 5)))

(defn part2 []
  (first (mine "bgvyzdsv" 6)))
