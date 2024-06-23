import sympy as sp
b = sp.symbols("b")
expr = ((b-3)*(b+3) + b + 20)
print(sp.expand(expr))