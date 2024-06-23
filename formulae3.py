import sympy as sp
a, b = sp.symbols("a b")
expr = (a**3 + b**3) + (a**3 - b**3)
print(sp.expand(expr))