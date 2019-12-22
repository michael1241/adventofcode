(ns adventofcode.day10
  (:require [clojure.java.io :as io]))

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
       (map indexes-of)
       (apply concat)
       set))
