import sympy as sp
a, b, c = sp.symbols("a b c")
exp = (a + b + c) ** 3
print(sp.expand(exp))
