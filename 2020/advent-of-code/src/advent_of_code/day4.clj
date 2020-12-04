(ns advent-of-code.day4
  (:require [advent-of-code.util :as util]))

(defn load-input-data []
  (->> (util/load-input 2020 4 #(map rest (re-seq #"(\S+):([\S]+)" %)))
       (partition-by empty?)
       (take-nth 2)
       (map #(apply hash-map (flatten %)))))

(defn required-fields? [passport]
  (every? #(contains? passport %) #{"byr" "iyr" "eyr" "hgt" "hcl" "ecl" "pid"}))

(defn check-year [passport field min max]
  (if-let [v (Integer/parseInt (passport field))]
    (and (>= v min)
         (<= v max))))

(defn valid-byr? [passport]
  (check-year passport "byr" 1920 2020))

(defn valid-iyr? [passport]
  (check-year passport "iyr" 2010 2020))

(defn valid-eyr? [passport]
  (check-year passport "eyr" 2020 2030))

(defn valid-hgt? [passport]
  (if-let [matches (re-matches #"(\d+)(cm|in)" (passport "hgt"))]
    (let [height (Integer/parseInt (nth matches 1)) unit (nth matches 2)]
      (case unit
        "cm" (<= 150 height 193)
        "in" (<= 59 height 76)))))

(defn valid-hcl? [passport]
  (not (nil? (re-matches #"#[0-9a-f]{6}" (passport "hcl")))))

(defn valid-ecl? [passport]
  (not (nil? (#{"amb" "blu" "brn" "gry" "grn" "hzl" "oth"} (passport "ecl")))))

(defn valid-pid? [passport]
  (not (nil? (re-matches #"\d{9}" (passport "pid")))))

(defn valid-passport? [passport]
  (and (required-fields? passport)
       (valid-byr? passport)
       (valid-iyr? passport)
       (valid-eyr? passport)
       (valid-hgt? passport)
       (valid-hcl? passport)
       (valid-ecl? passport)
       (valid-pid? passport)))

(defn part1 []
  (let [passports (load-input-data)]
    (count (filter required-fields? passports))))

(defn part2 []
  (let [passports (load-input-data)]
    (count (filter valid-passport? passports))))
