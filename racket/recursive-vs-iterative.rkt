#lang sicp

; recursive tree - f called inside +
(define (r n)
  (cond ((< n 3) n)
        (else (+ (* (r (- n 1)) 1)
                 (* (r (- n 2)) 2)
                 (* (r (- n 3)) 3))))
)

; iterative - uses a counter
(define (i n)
  (define (f n-1 n-2 n-3 steps)
    (cond ((< n 3) n)
          ((= steps 0) n-1)
          (else (f (+ n-1 (* 2 n-2) (* 3 n-3))
                   n-1
                   n-2
                   (- steps 1)))))
  (f 2 1 0 (- n 2))
)