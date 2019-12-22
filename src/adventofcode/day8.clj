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
