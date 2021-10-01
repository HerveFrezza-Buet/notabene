import notabene as nb

# Let us store here the formulas we will print.
formulas = []

# This function generates a name from a integer, but usually, you will
# identify your equation by an informative name. Names have to be
# compliant with latex syntax.
def name_of(idx) :
    a = idx % 26 + 65
    idx = idx // 26
    b = idx % 26 + 65
    idx = idx // 26
    c = idx % 26 + 65
    return chr(c) + chr(b) + chr(a)
    


# notabene handles formulas, that can be combined, reused, etc... So
# first, you need to build formulas from scratch. This is what nb.to
# does.

nb.set_displaystyle(True) # We set the displaystyle

x, y, n, i = nb.to('x y n i')
two        = nb.to(2)
sigma      = nb.to('\\sigma')

# Then, basic operators can be used to combine formulas... let us
# illustrate some of them and put some results in our list of
# formulas.

e = 1 + sigma**2 / (-(x+y)**(x-y) + x*y)
formulas.append(e)

euler = nb.math.e**(nb.math.i * nb.math.pi) + 1 == 0
formulas.append(euler)

# nb.seq build a formula that is a sequence of others.
formulas.append(nb.seq(x*y, x^y, x**y, x@y, x@(y,sigma), x == y))

sum1 = nb.math.sum(i==0, i <= n, 1/nb.math.fact(i) * x**i)
sum2 = nb.math.sum(nb.math.belongs(i, nb.math.N), 1 / i**2)
sum3 = nb.math.prod(nb.math.belongs(i, nb.math.N), 1 / i**2)
formulas.append(nb.seq(sum1, sum2, sum3))

# You can define functions.
fname = nb.to('f')@(nb.seq(sigma, i), nb.math.pi)
f = nb.fun(fname)
formulas.append(f(sum1+sum2))

# There are nice ways to define sets
formulas.append('A' == nb.math.set_ext(1, 2, ..., n))
B = nb.math.set_def(nb.math.belongs(x, nb.math.Q), f(x+3) > 38)
formulas.append(nb.to('B') == B)
indic_b = nb.math.indic(B)
formulas.append(indic_b(y))

# Min, max, ...
where = nb.math.belongs(y, B)
what = nb.fun('g')(y**2)
formulas.append(nb.math.max(where, what))
formulas.append(nb.math.min(where, what))
formulas.append(nb.math.argmax(where, what))
formulas.append(nb.math.argmin(where, what))



# Now, let us print our formulas in formulas.tex
with nb.files.defs('formulas.tex') as defs:
    defs.prefix = 'ex'
    for idx, expr in enumerate(formulas):
        defs[name_of(idx)] = expr

# Now you can have a look as example-001-001-getting-started.tex, and
# run latex to see the effect.



