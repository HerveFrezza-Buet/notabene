import notabene as nb


# notabene handles formulas, that can be combined, reused, etc... So
# first, you need to build formulas from scratch. This is what nb.to
# does.

x, y, n, i = nb.to('x y n i')
two        = nb.to(2)
sigma      = nb.to('\\sigma')

# Then, basic operators can be used to combine formulas... let us
# illustrate some of them and put some results in the file basics.tex.

# This is a trick to get nen command names
name_rank = 0
def new_name():
    global name_rank
    name = chr(65 + name_rank) # name = 'A', 'B', 'C', ...
    name_rank += 1
    return name

with nb.files.defs('basics.tex') as defs:
    nb.config.push('display style', True) # We set the displaystyle
    defs.prefix = 'ex'

    nb.config.push('product', None) #default
    defs[new_name()] = x*y
    
    nb.config.push('product', '.') 
    defs[new_name()] = x*y
    nb.config.pop() # pop the last config setting.
    # nb.config.pop('product') pops the last 'product' config setting. Similar to pop() here.
    
    nb.config.push('product', 'x') 
    defs[new_name()] = x*y
    nb.config.pop()
    
    e = 1 + sigma**2 / (-(x+y)**(x-y) + x*y)
    defs[new_name()] = e

    euler = nb.math.e**(nb.math.i * nb.math.pi) + 1 == 0
    defs[new_name()] = euler

    defs[new_name()] = nb.define(nb.math.i, nb.math.sqrt(-1))
    
    defs[new_name()] = nb.approx(nb.math.pi, 3.14)

    # Nice attributes are available
    e = nb.to([x+y])
    defs[new_name()] = nb.seq(e.bar, e.inv, e.T, e.star, e.plus, e.minus, e.prime)

    # nb.seq builds a formula that is a sequence of others.
    defs[new_name()] = nb.seq(x*y, x^y, x**y, x@y, x@(y,sigma), x == y)    

    # Quantifiers are available
    defs[new_name()] = nb.math.forall(x, x**2 >= 0)
    defs[new_name()] = nb.math.exists(x, x**2 == 0)

    # nb.cat concatenates formulas, nb.kat does the same with spacing.
    defs[new_name()] = nb.cat(x**2, y**3, x**n)
    defs[new_name()] = nb.kat(x**2, y**3, x**n)

    # Sum and products
    sum1 = nb.math.sum(i==0, i <= n, 1/nb.math.fact(i) * x**i)
    sum2 = nb.math.sum(nb.sets.isin(i, nb.sets.N), 1 / i**2)
    sum3 = nb.math.prod(nb.sets.isin(i, nb.sets.N), 1 / i**2)
    defs[new_name()] = nb.seq(sum1, sum2, sum3)

    # You can define functions.
    fname = nb.to('f')@(nb.seq(sigma, i), nb.math.pi)
    f = nb.fun(fname)
    defs[new_name()] = f(sum1+sum2)

    # Groups and tuples are made from lists... this may happen implicitely
    v = nb.to([n+1/n]) # explicit grouping formula from list.
    k = [n+1/n] ** n   # implicit grouping formula from list/
    defs[new_name()] = nb.seq(v, k)

    xy = [x, y, i, 3] # a list, not a formula.
    xy_t = xy**nb.text('hello world') # a list combined with a formula makes a formula.
    defs[new_name()] = xy_t
    
    # Delimiters can be added around formulas (the previous is for parentheses).
    x_2 = x ** 2
    defs[new_name()] = nb.seq(nb.math.abs(x_2),
                                 nb.math.norm(x_2),
                                 nb.math.matrix(x_2),
                                 nb.math.brace(x_2),
                                 nb.math.left_system(x_2),
                                 nb.math.right_system(x_2))

    # Layout arrange formulas as tabular. First is 'r', 'l', 'c' for
    # alignement, then the lines come.
    layout = nb.layout('c',
                       [n, n+1, n+2],
                       [x, x**2],
                       [nb.math.pi],
                       [1, 2, 3])
    defs[new_name()] = layout

    # This can be mixed nicely for a system of equations.
    eqs = nb.math.left_system(nb.layout('l',
                                        [x+1, nb.text('if'), x > 0],
                                        [x-1, nb.text('if'), x < 0],
                                        [38, nb.text('otherwise')]))
    defs[new_name()] = f(x) == eqs
    
    # This generates a latex cheetsheet that you can compile and display.
    defs.add_preamble('\\usepackage{color}') # You can add lines in the cheetsheet preamble.
    defs.add_preamble('\\usepackage{listings}') 
    defs.cheatsheet() 





