import math
from collections import ChainMap as Environment
import sys

Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Expression = (Atom, List)

class Procedure:
  def __init__(self, parameters, body, environment):
    self.parameters, self.body, self.environment = parameters, body, environment
  
  def __call__(self, *arguments):
    environment = Environment(dict(zip(self.parameters, arguments)), self.environment)
    return evaluate(self.body, environment)

def division_operator(x, y):
  if isinstance(x, float) and isinstance(y, float):
    return x / y
  return []

def multiplication_operator(x, y):
  if isinstance(x, float) and isinstance(y, float) or isinstance(x, int) and isinstance(y, int):
    return x * y
  return []

def equality_operator(x, y):
  if isinstance(x, float) and isinstance(y, float) or isinstance(x, int) and isinstance(y, int):
    return 1 if x == y else 0
  return []

def greater_operator(x, y):
  if isinstance(x, float) and isinstance(y, float) or isinstance(x, int) and isinstance(y, int):
    return 1 if x > y else 0
  return []

def lesser_operator(x, y):
  if isinstance(x, float) and isinstance(y, float) or isinstance(x, int) and isinstance(y, int):
    return 1 if x < y else 0
  return []

def greater_or_equal_operator(x, y):
  if isinstance(x, float) and isinstance(y, float) or isinstance(x, int) and isinstance(y, int):
    return 1 if x >= y else 0
  return []

def lesser_or_equal_operator(x, y):
  if isinstance(x, float) and isinstance(y, float) or isinstance(x, int) and isinstance(y, int):
    return 1 if x <= y else 0
  return []

def subtraction_operator(x, y):
  if isinstance(x, float) and isinstance(y, float) or isinstance(x, int) and isinstance(y, int):
    return x - y
  return []

def addition_operator(x, y):
  if isinstance(x, float) and isinstance(y, float) or isinstance(x, int) and isinstance(y, int):
    return x + y
  return []

def range_procedure(start, stop, step):
  result = []
  r = start
  while r <= stop:
      result.append(r)
      r += step
  return result

def standard_environment():
  environment = {}
  environment.update(vars(math))
  environment.update({
    '+': addition_operator,
    '-': subtraction_operator,
    '*': multiplication_operator,
    '/': division_operator, 
    '>': greater_operator,
    '<': lesser_operator,
    '>=': greater_or_equal_operator,
    '<=': lesser_or_equal_operator,
    '=': equality_operator,

    'apply': lambda procedure, arguments: procedure(*arguments),
    'begin': lambda *x: x[-1],
    'car': lambda x: x[0],
    'cdr': lambda x: x[1:], 
    'cons': lambda x, y: [x] + y,
    'list': lambda *x: list(x),
    'print': lambda x: print(lisply_string(x)),
    'range': range_procedure,

    'list?': lambda x: 1 if isinstance(x, List) else 0, 
    'null?': lambda x: 1 if x == [] else 0,
    'real?': lambda x: 1 if isinstance(x, float) else 0,
    'integral?': lambda x: 1 if isinstance(x, int) else 0,
    'lambda?': lambda x: 1 if callable(x) else 0,
    'symbol?': lambda x: 1 if isinstance(x, Symbol) else 0
  })
  return environment

global_environment = standard_environment()

def tokenize(chars: str) -> list:
  return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program: str) -> Expression:
  return read_from_tokens(tokenize(program))

def read_from_tokens(tokens: list) -> Expression:
  if len(tokens) == 0:
    raise SyntaxError('Unexpected end of file.')
  token = tokens.pop(0)
  if token == '(':
    L = []
    while tokens[0] != ')':
      L.append(read_from_tokens(tokens))
    tokens.pop(0)
    return L
  elif token == ')':
    raise SyntaxError('Unexpected `)`')
  else:
    return atom(token)
  
def atom(token: str) -> Atom:
  try: return int(token)
  except ValueError:
    try: return float(token)
    except ValueError:
      return Symbol(token)

def evaluate(x: Expression, environment = global_environment) -> Expression:
  if isinstance(x, Symbol):
    return environment[x]
  elif not isinstance(x, List):
    return x
  elif x[0] == 'quote':
    (_, expression) = x
    return expression
  elif x[0] == 'if':
    (_, test, consequence, alternative) = x
    test_result = evaluate(test, environment)
    if test_result is 0:
      return evaluate(alternative, environment)
    elif test_result is 1:
      return evaluate(consequence, environment)
    raise ValueError('Test expression should evaluate to either 0 or 1 in conditional expression.')
  elif x[0] == 'define':
    (_, variable, expression) = x
    environment[variable] = evaluate(expression, environment)
  elif x[0] == 'lambda':
    (_, parameters, body) = x
    return Procedure(parameters, body, environment)
  else:
    procedure = evaluate(x[0], environment)
    arguments = [evaluate(expression, environment) for expression in x[1:]]
    return procedure(*arguments)

def repl(prompt = 'Lisply > '):
  while True:
    try: value = evaluate(parse(input(prompt)))
    except Exception:
      print('Error evaluating an expression.')
      continue
    if value is not None:
      print(lisply_string(value))

def lisply_string(expression):
  if isinstance(expression, List):
    return '(' + ' '.join(map(lisply_string, expression)) + ')'
  else:
    return str(expression)

def main(args):
  if len(args) == 1:
    repl()
  elif len(args) == 2:
    path = args[1]
    with open(path, 'r') as file:
      data = file.read()
    evaluate(parse(data))
  else:
    print('Too many arguments.')

if __name__ == '__main__':
  main(sys.argv)