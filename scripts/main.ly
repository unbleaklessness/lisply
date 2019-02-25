(begin
  (define null (list))
  
  (define abs (lambda (x)
    (if (< x 0) (* x -1) x)))

  (define true 1)
  (define false 0)

  (define not (lambda (x)
    (if x false true)))
  (define and (lambda (a b)
    (if a (if b true false) false)))
  (define or (lambda (a b)
    (if a true (if b true false))))

  (define map (lambda (f l)
    (if (and (lambda? f) (list? l))
      (if (not (null? l))
        (cons (f (car l)) (map f (cdr l)))
        null)
      null)))
  
  (define length (lambda (x) 
    (if (list? x)
      (if (not (null? x))
        (+ 1 (length (cdr x)))
        0)
      null)))

  (define concatenate (lambda (l1 l2)
      (if (null? l1)
        l2
        (cons (car l1)
              (concatenate (cdr l1) l2)))))
  )