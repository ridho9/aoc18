#lang racket

(call-with-input-file "input"
    (lambda (in)
        (define s (string-split (port->string in)))
        (define m (map string->number s))
        (define res (foldl + 0 m))
        (writeln res)))