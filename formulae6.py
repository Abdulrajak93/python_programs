import sympy as sp
b = sp.symbols("b")
expr = b ** 2 + 2 - 27
print(sp.solve(expr))

