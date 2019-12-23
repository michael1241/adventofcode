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

(defn get-gradient
  [[x1 y1] [x2 y2]]
  (if (= x1 x2)
    (cond
      (> y1 y2) -1
      (< y1 y2)  1)
    (/ (- y2 y1) (- x2 x1))))

(defn get-b
  [[x1 y1] g]
  (- y1 (* g x1)))

(defn blocking?
  [[[x1 y1] [x2 y2]] [x3 y3]]
  (let [g (get-gradient [x1 y1] [x2 y2])
        b (get-b [x1 y1] g)]
    (and (= y3 (+ (* x3 g) b))
         (<= (min x1 x2) x3 (max x1 x2))
         (<= (min y1 y2) y3 (max y1 y2))
         (not (or (= [x1 y1] [x3 y3]) (= [x2 y2] [x3 y3]))))))

(defn any-block?
  [[[x1 y1] [x2 y2]]]
  (some true? (map #(blocking? [[x1 y1] [x2 y2]] %) asteroid-coords)))

(def clear-paths (remove any-block? asteroid-pairs))

(def most-connections
  (->> clear-paths
       (apply concat)
       frequencies
       (apply max-key second)))
