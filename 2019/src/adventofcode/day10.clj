(ns adventofcode.day10
  (:require [clojure.java.io :as io])
  (:require [clojure.math.combinatorics :as combo]))

(def asteroids
  (-> "inputday10"
    io/resource
    io/reader
    slurp
    clojure.string/split-lines))

(defn indexes-of [indexed-row-data]
  (let [[y row-data] indexed-row-data]
    (->> row-data
         (map-indexed vector)
         (filter #(= (second %) \#))
         (map first)
         (map #(vector y %)))))

(def asteroid-coords
  (->> asteroids
       (map-indexed vector)
       (mapcat indexes-of)
       set))

(def asteroid-pairs (combo/combinations asteroid-coords 2))

(defn cross-prod
  [[x1 y1] [x2 y2] [x3 y3]]
  (- (* (- y3 y1) (- x2 x1)) (* (- x3 x1) (- y2 y1))))

(defn dot-prod
  [[x1 y1] [x2 y2] [x3 y3]]
  (+ (* (- x3 x1) (- x2 x1)) (* (- y3 y1) (- y2 y1))))

(defn squared-length
  [[x1 y1] [x2 y2]]
  (+ (* (- x2 x1) (- x2 x1)) (* (- y2 y1) (- y2 y1))))

(defn blocking?
  [[[x1 y1] [x2 y2]] [x3 y3]]
  (let [crossprod   (cross-prod [x1 y1] [x2 y2] [x3 y3])
        dotprod     (dot-prod [x1 y1] [x2 y2] [x3 y3])
        squaredlen  (squared-length [x1 y1] [x2 y2])]
    (and (zero? crossprod)
         (>= dotprod 0)
         (<= dotprod squaredlen)
         (and (not= [x1 y1] [x3 y3]) (not= [x2 y2] [x3 y3])))))

(defn any-block?
  [[[x1 y1] [x2 y2]]]
  (some true? (map #(blocking? [[x1 y1] [x2 y2]] %) asteroid-coords)))

(def clear-paths (remove any-block? asteroid-pairs))

(def most-connections
  (->> clear-paths
       (apply concat)
       frequencies
       (apply max-key second)))
;[[20 20] 292]
