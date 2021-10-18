import notabene as nb


# notabene handles formulas, that can be combined, reused, etc... So
# first, you need to build formulas from scratch. This is what nb.to
# does.

x, y, n, i = nb.to('x y n i')
two        = nb.to(2)
sigma      = nb.to('\\sigma')

# Then, basic operators can be used to combine formulas... let us
# illustrate some of them and put some results in the file basics.tex.
# We name latex commands \exA, \exB... thanks chr(65+i).

with nb.files.defs('basics.tex') as defs:
    nb.set_displaystyle(True) # We set the displaystyle
    defs.prefix = 'ex'
    idx = 0

    nb.set_product_mode(None) #default
    defs[chr(65 + idx)] = x*y
    idx += 1
    
    nb.set_product_mode('.') 
    defs[chr(65 + idx)] = x*y
    idx += 1
    
    nb.set_product_mode('x') 
    defs[chr(65 + idx)] = x*y
    idx += 1
    
    nb.set_product_mode(None)
    
    e = 1 + sigma**2 / (-(x+y)**(x-y) + x*y)
    defs[chr(65 + idx)] = e
    idx += 1

    euler = nb.math.e**(nb.math.i * nb.math.pi) + 1 == 0
    defs[chr(65 + idx)] = euler
    idx += 1

    defs[chr(65 + idx)] = nb.define(nb.math.i, nb.math.sqrt(-1))
    idx += 1

    # nb.seq builds a formula that is a sequence of others.
    defs[chr(65 + idx)] = nb.seq(x*y, x^y, x**y, x@y, x@(y,sigma), x == y)
    idx += 1

    # Quantifiers are available
    defs[chr(65 + idx)] = nb.math.forall(x, x**2 >= 0)
    idx += 1
    defs[chr(65 + idx)] = nb.math.exists(x, x**2 == 0)
    idx += 1

    # nb.cat concatenates formulas, nb.kat does the same with spacing.
    defs[chr(65 + idx)] = nb.cat(x**2, y**3, x**n)
    idx += 1
    defs[chr(65 + idx)] = nb.kat(x**2, y**3, x**n)
    idx += 1

    # Sum and products
    sum1 = nb.math.sum(i==0, i <= n, 1/nb.math.fact(i) * x**i)
    sum2 = nb.math.sum(nb.sets.isin(i, nb.sets.N), 1 / i**2)
    sum3 = nb.math.prod(nb.sets.isin(i, nb.sets.N), 1 / i**2)
    defs[chr(65 + idx)] = nb.seq(sum1, sum2, sum3)
    idx += 1

    # You can define functions.
    fname = nb.to('f')@(nb.seq(sigma, i), nb.math.pi)
    f = nb.fun(fname)
    defs[chr(65 + idx)] = f(sum1+sum2)
    idx += 1

    # Groups and tuples are made from lists... this may happen implicitely
    v = nb.to([n+1/n]) # explicit grouping formula from list.
    k = [n+1/n] ** n   # implicit grouping formula from list/
    defs[chr(65 + idx)] = nb.seq(v, k)
    idx += 1

    xy = [x, y, i, 3] # a list, not a formula.
    xy_t = xy**nb.text('hello world') # a list combined with a formula makes a formula.
    defs[chr(65 + idx)] = xy_t
    idx += 1

    # Delimiters can be added around formulas (the previous is for parentheses).
    x_2 = x ** 2
    defs[chr(65 + idx)] = nb.seq(nb.math.abs(x_2),
                                 nb.math.norm(x_2),
                                 nb.math.matrix(x_2),
                                 nb.math.left_system(x_2),
                                 nb.math.right_system(x_2))
    idx += 1

    # Layout arrange formulas as tabular. First is 'r', 'l', 'c' for
    # alignement, then the lines come.
    layout = nb.layout('c',
                       [n, n+1, n+2],
                       [x, x**2],
                       [nb.math.pi],
                       [1, 2, 3])
    defs[chr(65 + idx)] = layout
    idx += 1

    # This can be mixed nicely for a system of equations.
    eqs = nb.math.left_system(nb.layout('l',
                                        [x+1, nb.text('if'), x > 0],
                                        [x-1, nb.text('if'), x < 0],
                                        [38, nb.text('otherwise')]))
    defs[chr(65 + idx)] = f(x) == eqs
    idx += 1

    defs.cheatsheet() # This generates a latex cheetsheet that you can compile and display.





