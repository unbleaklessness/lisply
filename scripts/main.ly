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

  (define all-true (lambda (l)
    (if (list? l)
      (if (null? l)
        true
        (and (car l) (all-true (cdr l))))
      null)))
  
  (print (quote (All true test)))
  (print (= (all-true (list true true true)) true))
  (print (not (= (all-true (list true false true)) true)))

  (define length (lambda (x) 
    (if (list? x)
      (if (null? x)
        0
        (+ 1 (length (cdr x))))
      null)))
  
  (print (quote (Length test)))
  (print (= (length (list 1 2 3 4 5)) 5))

  (define lists-equal (lambda (l1 l2)
    (if (= (length l1) (length l2))
      (if (null? l1)
        true
        (all-true (list
          (= (car l1) (car l2))
          (lists-equal (cdr l1) (cdr l2)))))
    false)))
  
  (print (quote (Lists equal test)))
  (print (lists-equal (list 1 2 3 4) (list 1 2 3 4)))
  (print (not (lists-equal (list 1 2 7 4) (list 1 2 3 4))))

  (define map (lambda (f l)
    (if (and (lambda? f) (list? l))
      (if (not (null? l))
        (cons (f (car l)) (map f (cdr l)))
        null)
      null)))
  
  (print (quote (Map test)))
  (print (lists-equal (map (lambda (x) (+ x 1)) (list 1 2 3 4)) (list 2 3 4 5)))

  (define concatenate (lambda (l1 l2)
      (if (null? l1)
        l2
        (cons (car l1)
              (concatenate (cdr l1) l2)))))
  
  (print (quote (Concatenate test)))
  (print (lists-equal (concatenate (list 1 2 3) (list 4 5 6)) (list 1 2 3 4 5 6)))

  (define foldl (lambda (f a l)
    (if (all-true (list (lambda? f) (list? l)))
      (if (null? l)
        a
        (foldl f (f a (car l)) (cdr l)))
      null)))

  (print (quote (Foldl test)))
  (print (= (foldl (lambda (x y) (+ x y)) 0 (list 1 2 3 4 5)) 15))

  (define foldr (lambda (f a l) 
    (if (all-true (list (lambda? f) (list? l)))
      (if (null? l)
        a
        (f (car l) (foldr f a (cdr l))))
      null)))
  
  (print (quote (Foldr test)))
  (print (= (foldr (lambda (x y) (+ x y)) 0 (list 1 2 3 4 5)) 15))

  (define when (lambda (p e)
    (if p e null)))

  (print (quote (When test)))
  (print (= (when (= 1 1) 1) true))
  (print (null? (when (= 1 2) 1)))
  
  (print (quote (Range test)))
  (print (lists-equal (range 1 10 1) (list 1 2 3 4 5 6 7 8 9 10)))

  (define in-range (lambda (n from to)
    (or (>= n from) (<= n to))))
  
  (print (quote (In range test)))
  (print (in-range 0.5 0.0 1.0))

  (define integrate (lambda (f from to step)
    (foldl
      (lambda (a x) (+ a (* step (f x))))
      0.0
      (range from to step))))

  (print (quote (Integrate test)))
  (print (in-range (integrate (lambda (x) (* x x)) 0.0 1.0 0.01) 0.32 0.34))
  )