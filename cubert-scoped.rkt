#lang sicp

(define (cubert x)
  
  ; Newton's method
  (define (cubert-iter guess)
    (if (good-enough? guess)
      guess
      (cubert-iter (improve guess))))
  
  (define (good-enough? guess)
    (< (abs (- (/ (expt guess 3) x) 1)) (expt 10 -9)))

  (define (improve y)
    (/ (+ (/ x (* y y)) (* 2 y)) 3))
  
  (cubert-iter 1.0) ; 1.0 is initial seed
)