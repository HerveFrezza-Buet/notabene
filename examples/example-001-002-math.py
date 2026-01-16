import notabene as nb


x, i, n = nb.to('x i n')
x_2 = x**2

with nb.files.defs('001-002-math.tex') as defs:
    nb.config.push('display style', True) # We set the displaystyle
    defs.prefix = 'ex'
    
    defs['Constants'] = nb.seq(nb.math.pi, nb.math.i, nb.math.e, nb.math.infinity)
    defs['Functions'] = nb.seq(nb.math.exp(x), nb.math.min(x, x_2, n), nb.math.max(x, x_2, i, n, n**2))
    defs['Euler'] = nb.math.e**(nb.math.i * nb.math.pi) + 1 == 0
    
    # Quantifiers are available
    defs['Forall'] = nb.math.forall(x, x**2 >= 0)
    defs['Exists'] = nb.math.exists(x, x**2 == 0)

    # Such as is also available
    defs['SuchAsOne'] = x.isin('X').such_as(x > 0)                   # with such_as method
    defs['SuchAsTwo'] = nb.math.such_as(nb.sets.isin(x, 'X'), x > 0) # with functions.
    
    # Delimiters can be added around formulas.
    x_2 = x ** 2
    defs['Formulas'] = nb.seq([x_2],
                              nb.math.abs(x_2),
                              nb.math.sqrt(x_2),
                              nb.math.root(x_2, 13),
                              nb.math.norm(x_2),
                              nb.math.matrix(x_2),
                              nb.math.brace(x_2),
                              nb.math.bracket(x_2),
                              nb.math.left_system(x_2),
                              nb.math.right_system(x_2))

    # Functions
    f, g, h = nb.fun('f g h')
    fgh = nb.math.compose(f, g, h)
    defs["FunComp"] = nb.seq(f.name, g.name, h.name, fgh.name, fgh(x, x_2))
    
    # Sum and products
    sum1 = nb.math.sum(i==0, i <= n, 1/nb.math.fact(i) * x**i)
    sum2 = nb.math.sum(nb.sets.isin(i, nb.sets.N), 1 / i**2)
    prod = nb.math.prod(nb.sets.isin(i, nb.sets.N), 1 / i**2)
    defs['SumProd'] = nb.seq(sum1, sum2, prod)

    # Argmin and argmax (see sets)
    where = nb.sets.isin(x, nb.sets.C)
    what = nb.fun('g')(x**2)
    defs['Args'] = nb.seq(nb.sets.max(where, what),
                          nb.sets.min(where, what),
                          nb.sets.argmax(where, what),
                          nb.sets.argmin(where, what))
    

    # This can be mixed nicely for a system of equations.
    eqs = nb.math.left_system(nb.layout('l',
                                        [x+1, nb.text('if'), x > 0],
                                        [x-1, nb.text('if'), x < 0],
                                        [38, nb.text('otherwise')]))
    defs['SystemA'] = nb.fun('f')(x) == eqs

    defs['SystemB'] = nb.math.left_system(nb.layout('rcl',
                                                    [nb.math.pi, nb.define_symbol, 3.141592654],
                                                    [nb.to([x+1])**2, '=', x**2 + 2*x + 1]))
    
    defs['Braces'] = nb.seq(nb.math.overbrace( nb.seq(  1, ...,  99), nb.text('over')),
                            nb.math.underbrace(nb.seq(100, ..., 199), nb.text('under')))
    
    # This generates a latex cheetsheet that you can compile and display.
    defs.cheatsheet() 





