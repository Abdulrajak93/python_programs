import sympy as sp
x = sp.symbols("x")
expr = x/4 + x/5 -9
print(sp.solve(expr))