#lang sicp

(define (p row col)
  (cond ((= col 0) 1)
        ((= col row) 1)
        (else (+ (p (- row 1) (- col 1))
                 (p (- row 1) col)))))