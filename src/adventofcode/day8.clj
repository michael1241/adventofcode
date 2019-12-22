(ns adventofcode.day8
  (:require [clojure.java.io :as io]))

(def pixels
  (-> "inputday8"
    io/resource
    io/reader
    slurp))

(def layer-size (* 25 6)) ;150

(def layers (partition layer-size pixels))

(defn count-digit
  [layer digit]
  (->> layer
       (filter #(= digit %))
       count))

(defn count-digits
  [digits layer]
  (map #(count-digit layer %) digits))

(def layer-counts (map #(count-digits [\0 \1 \2] %) layers))

(apply min-key first layer-counts) ;(5 15 130)

(* 15 130) ;1950

(defn first-non-transparent
  [pixel-stack]
  (->> pixel-stack
      (filter #(not (= % \2)))
      first))
;(some #{\1 \2} [\1 \2 \3 \4]) idiomatic way

(def image-pixels (map first-non-transparent (apply map vector layers)))

(map println (partition 25 image-pixels))
