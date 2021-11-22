#lang sicp

; Newton's method
(define (cubert-iter guess x)
  (if (good-enough? guess (improve guess x))
      guess
      (cubert-iter (improve guess x) x))
)

(define (improve y x)
  (/ (+ (/ x (* y y)) (* 2 y)) 3)
)

(define (good-enough? guess next-guess)
  (< (abs (- (/ guess next-guess) 1)) (expt 10 -9))
)

(define (cubert x)
  (cubert-iter 1.0 x) ; 1.0 is initial seed
)