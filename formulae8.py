import sympy as sp
x = sp.symbols("x")
expr = (x ** 2)*(x + 3) ** 2
for num in [1, 2, 3, 4, 5]:
    print(expr.subs(x, num))