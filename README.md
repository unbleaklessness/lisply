Based on: [(How to Write a (Lisp) Interpreter (in Python))](http://norvig.com/lispy.html).

# Lisply description:

## Lisply expressions:

- Variable reference:
  - `symbol`.
  - A symbol is interpreted as a variable name; its value is the variable's value. Example: `r` -> `10` (assuming `r` was previously defined to be `10`).
- Constant literal:
  - `number`.
  - A number evaluates to itself. Examples: `12` -> `12` or `-3.45e+6` -> `-3.45e+`.
- Conditional:
  - `(if test conseq alt)`.
  - Evaluate test; if true, evaluate and return conseq; otherwise alt. Example: `(if (> 10 20) (+ 1 1) (+ 3 3))` -> `6`.
- Definition:
  - Syntax: `(define symbol exp)`.
  - Define a new variable and give it the value of evaluating the expression exp. Examples: `(define r 10)`.
- Procedure call:
  - `(proc arg...)`.
  - If proc is anything other than the symbols if or define then it is treated as a procedure. Evaluate proc and all the args, and then the procedure is applied to the list of arg values. Example: `(sqrt (* 2 8))` -> `4.0`.