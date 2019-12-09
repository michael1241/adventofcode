(ns adventofcode.day4
  (:gen-class))

(defn digits
  "split number into digits with end and lead buffer"
  [number]
  (concat '(-1) (map #(Character/digit % 10) (str number)) '(10)))

(defn pairs
  "split number into pairs of digits (step size 1)"
  [number]
  (partition 2 1 (digits number)))

(defn quads
  "split number into quads of digits (step size 1) with lead and end buffer"
  [number]
  (partition 4 1 (digits number)))

(defn equality
  [nums]
  (= (nth nums 0) (nth nums 1)))

(defn equality-quads
  [nums]
  (let [d1 (nth nums 0)
        d2 (nth nums 1)
        d3 (nth nums 2)
        d4 (nth nums 3)]
    (and (= d2 d3) (not= d1 d2) (not= d3 d4))))

(defn increasing
  [nums]
  (<= (nth nums 0) (nth nums 1)))

(defn adjacent-digits-equal
  [pairs]
  (not-every? false? (map equality pairs)))

(defn adjacent-digits-equal-not-triple
  [quads]
  (not (every? false? (map equality-quads quads))))

(defn increasing-digits
  [pairs]
  (every? true? (map increasing pairs)))

;; range 367479-893698

(defn check-num
  [number]
  (let [pairs (pairs number)
        quads (quads number)]
    (and (increasing-digits pairs) (adjacent-digits-equal-not-triple quads))))

(count (filter check-num (range 367479 893698)))
