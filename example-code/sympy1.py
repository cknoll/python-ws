import sympy as sp
x = sp.Symbol("x")
a, b, c, z = sp.symbols("a b c z") # create several symbols at once

some_formula = a*b*x*b + b**2*a*x - c*b*(2*a/c*x*b-1/(b*2))
print(some_formula) # -> -b*c*(-1/(2*b) + 2*a*b*x/c) + 2*a*x*b**2
print(some_formula.expand()) # -> c/2 

# some calculus
y = sp.sin(x)*sp.exp(3*x)*sp.sqrt(a)
print(y) # -> a**(1/2)*exp(x)*sin(x)

# derive
y.diff(x) # -> 3*sqrt(a)*exp(3*x)*sin(x) + sqrt(a)*exp(3*x)*cos(x)

# trigonometric simplification
print(sp.trigsimp(sp.sin(x)**2+sp.cos(x)**2)) # -> 1

# substitution

# 2 arguments:
# substitute x with z-1
y2 = y.subs(x, z-1)

# 1 argument (list of 2-tuples):
# substitute x with z-1 and a with 25 (in this order)
y3 = y.subs([(x, z-1), (a, 25)])
