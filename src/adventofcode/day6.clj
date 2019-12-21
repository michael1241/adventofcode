(ns adventofcode.day6
  (:require [clojure.java.io :as io]))

(def orbits-string
  (-> "inputday6"
    io/resource
    io/reader
    slurp
    clojure.string/split-lines))

(defn orbits-string-to-orbits
  [in]
  (loop [orbit (first in)
         remaining (rest in)
         orbits {}]
    (if (nil? orbit)
      orbits
      (recur (first remaining) (rest remaining) (assoc orbits (subs orbit 4 7) (subs orbit 0 3))))))

;map where key orbits value
(def orbits (orbits-string-to-orbits orbits-string))

(defn trace
  [orbits
   firstbody]
  (loop [body firstbody
         path []
         chain 0]
    (let [nextbody (get orbits body)]
      (if (nil? nextbody)
        [chain path]
        (recur nextbody (conj path nextbody) (inc chain))))))

(defn count-system
  [orbits]
  (loop [orbit (first orbits)
         remaining (rest orbits)
         total 0]
    (if (nil? orbit)
      total
      (recur (first remaining) (rest remaining) (->> orbit
                                                    first
                                                    (trace orbits)
                                                    first
                                                    (+ total))))))

(def santapath (last (trace orbits "SAN"))) ;250 long
(def santaset (set santapath))

(def mypath (last (trace orbits "YOU"))) ;253 long
(def myset (set mypath))

(count (clojure.set/intersection santaset myset)) ;62
(- (+ 250 253) (* 2 62)) ;379
