(ns adventofcode.day1
  (:require [clojure.java.io :as io] ))

(defn fuel-req
  "work out how much fuel is needed based on mass"
  [mass]
  (- (quot mass 3) 2))

(defn fuel-req-recur
  "use fuel-req to calculate fuel needed based on mass including fuel mass"
  [startmass]
  (loop [mass startmass
         totalfuel []]
    (let [newmass (fuel-req mass)]
      (if (< (int newmass) 1)
        (reduce + totalfuel)
        (recur newmass (conj totalfuel newmass))))))

(defn f []
  (with-open [rdr (io/reader (io/resource "inputday1"))]
    (reduce + (map fuel-req-recur (map read-string (line-seq rdr))))))

