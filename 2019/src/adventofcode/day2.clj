(ns adventofcode.day2)

(def initialinput [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,19,6,23,2,13,23,27,1,9,27,31,2,31,9,35,1,6,35,39,2,10,39,43,1,5,43,47,1,5,47,51,2,51,6,55,2,10,55,59,1,59,9,63,2,13,63,67,1,10,67,71,1,71,5,75,1,75,6,79,1,10,79,83,1,5,83,87,1,5,87,91,2,91,6,95,2,6,95,99,2,10,99,103,1,103,5,107,1,2,107,111,1,6,111,0,99,2,14,0,0])

;before running the program, replace position 1 with the value 12 and replace position 2 with the value 2
(def input (assoc initialinput 1 12 2 2))

(def target 19690720)

(defn change-vec
  "return new vector vec given modification based on position p, or first vec value if terminating condition"
  [vec
   p]
  (case (nth vec p)
    1 (assoc vec (nth vec (+ p 3)) (+ (nth vec (nth vec (+ p 1))) (nth vec (nth vec (+ p 2)))))
    2 (assoc vec (nth vec (+ p 3)) (* (nth vec (nth vec (+ p 1))) (nth vec (nth vec (+ p 2)))))
    99 (nth vec 0)
    ))

(defn computer
  "runs through input and returns first vec value at termination"
  [input]
  (loop [position 0
         vec input]
    (let [output (change-vec vec position)]
      (if-not (vector? output)
        output
        (recur (+ position 4) output)))))

(def pairs
  (for [noun (range 100)
        verb (range 100)]
    [(int noun) (int verb)]))

(defn noun-verb
  "test noun verb in range 0 99 to find input that produces desired result"
  [input
   pairs]
  (loop [vec input
         pair (nth pairs 0)
         nextpair 1]
    (let [vec (assoc vec 1 (nth pair 0) 2 (nth pair 1))]
      (if (== (computer vec) target)
        pair
        (recur input (nth pairs nextpair) (inc nextpair))))))

(noun-verb input pairs)
