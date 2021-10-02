import notabene as nb

# Let us store here the formulas we will print.
formulas = []

# notabene handles formulas, that can be combined, reused, etc... So
# first, you need to build formulas from scratch. This is what nb.to
# does.

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

# nb.seq builds a formula that is a sequence of others.
formulas.append(nb.seq(x*y, x^y, x**y, x@y, x@(y,sigma), x == y))

# Quantifiers are available
formulas.append(nb.math.forall(x, x**2 >= 0))
formulas.append(nb.math.exists(x, x**2 == 0))

# nb.cat concatenates formulas, nb.kat does the same with spacing.
formulas.append(nb.cat(x**2, y**3, x**n))
formulas.append(nb.kat(x**2, y**3, x**n))

sum1 = nb.math.sum(i==0, i <= n, 1/nb.math.fact(i) * x**i)
sum2 = nb.math.sum(nb.sets.isin(i, nb.sets.N), 1 / i**2)
sum3 = nb.math.prod(nb.sets.isin(i, nb.sets.N), 1 / i**2)
formulas.append(nb.seq(sum1, sum2, sum3))

# You can define functions.
fname = nb.to('f')@(nb.seq(sigma, i), nb.math.pi)
f = nb.fun(fname)
formulas.append(f(sum1+sum2))

# Groups and tuples are made from lists... this may happen implicitely
v = nb.to([n+1/n]) # explicit grouping formula from list.
k = [n+1/n] ** n   # implicit grouping formula from list/
formulas.append(nb.seq(v, k))

xy = [x, y, i, 3] # a list, not a formula.
xy_t = xy**nb.text('hello world') # a list combined with a formula makes a formula.
formulas.append(xy_t)

# Delimiters can be added around formulas (the previous is for parentheses).
x_2 = x ** 2
formulas.append(nb.seq(nb.math.abs(x_2),
                       nb.math.norm(x_2),
                       nb.math.matrix(x_2),
                       nb.math.left_system(x_2),
                       nb.math.right_system(x_2)))

# Layout arrange formulas as tabular. First is 'r', 'l', 'c' for
# alignement, then the lines come.
layout = nb.layout('c',
                   [n, n+1, n+2],
                   [x, x**2],
                   [nb.math.pi],
                   [1, 2, 3])
formulas.append(layout)

# This can be mixed nicely for a systel of equations.
eqs = nb.math.left_system(nb.layout('l',
                                    [x+1, nb.text('if'), x > 0],
                                    [x-1, nb.text('if'), x < 0],
                                    [38, nb.text('otherwise')]))
formulas.append(f(x) == eqs)


# Now, let us print our formulas in formulas.tex

with nb.files.defs('formulas.tex') as defs:
    nb.set_displaystyle(True) # We set the displaystyle
    defs.prefix = 'ex'
    for idx, expr in enumerate(formulas):
        defs[chr(65 + idx)] = expr # we use exA, exB, exC... as names.
    defs.cheatsheet() # generates a latex cheetsheet that you can compile.





