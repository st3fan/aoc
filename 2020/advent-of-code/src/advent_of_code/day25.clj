(ns advent-of-code.day25)

(def card-key 6930903)
(def door-key 19716708)

(defn transform-subject-number [subject-number loop-size]
  (loop [index loop-size value 1]
    (if (zero? index)
      value
      (recur (dec index)
             (mod (* value subject-number) 20201227)))))

(defn find-loop-size [subject-number public-key]
  (loop [value 1 loop-size 1]
    (let [value (mod (* value subject-number) 20201227)]
      (if (= value public-key)
        loop-size
        (recur value (inc loop-size))))))

(defn part1 []
  (let [loop-size (find-loop-size 7 card-key)]
    (transform-subject-number door-key loop-size)))
