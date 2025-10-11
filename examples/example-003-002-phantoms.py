import notabene as nb

x, y, i, n = nb.to('x y i n')
with nb.files.defs('003-002-phantoms.tex') as defs:
    nb.config.push('display style', True) # We set the displaystyle
    defs.prefix = 'ex'

    a = x**y
    b = x@y
    c = x/y
    d = nb.math.sum(i, n, x**i)

    defs['Bad'] = nb.math.sqrt(a) \
        + nb.math.sqrt(b)         \
        + nb.math.sqrt(c)         \
        + nb.math.sqrt(d)

    valign = nb.phantom.vertical(a, b, c, d) # Alignement is made according to these.
    defs['Good'] = nb.math.sqrt(valign(a)) \
        + nb.math.sqrt(valign(b))          \
        + nb.math.sqrt(valign(c))          \
        + nb.math.sqrt(valign(d))
    

    # This generates a latex cheetsheet that you can compile and display.
    defs.cheatsheet() 
