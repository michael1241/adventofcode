(ns day4
  (:gen-class))

(defn digits
  [number]
  (map #(Character/digit % 10) (str number))) ;don't understand how this works...

(defn pairs
  [number]
  (partition 2 1 (digits number)))

(defn equality
  [nums]
  (if (= (nth nums 0) (nth nums 1)) true false))

(defn increasing
  [nums]
  (if ()))

(defn adjacent-digits
  [pairs]
  (not-every? false? (map #(equality %) pairs)))

(defn increasing-digits
  [pairs]
  )
