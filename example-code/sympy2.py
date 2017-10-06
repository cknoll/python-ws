import sympy as sp
from ipydex import IPS

a, b, c, x = sp.symbols("a b c x") # create symbols

# define expression
f = a*sp.sin(b*x)

# create python-function
f_xa_fnc = sp.lambdify((a, b, x), f, modules="numpy")

# evaluate function
print(f_xa_fnc(1.2, 0.5, 3.14))

IPS()
# use magic commands to investigate speedup
# %time f_xa_fnc(1, 1, 1)
# %time f.subs([(a, 1), (b, 1), (x, 1)]).evalf()

