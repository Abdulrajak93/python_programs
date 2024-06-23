import sympy as sp
x = sp.symbols("x")
expr = x * (x+2) 
print(sp.expand(expr))