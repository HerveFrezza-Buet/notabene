import notabene as nb


# notabene handles formulas, that can be combined, reused, etc... So
# first, you need to build formulas from scratch. This is what nb.to
# does.

x, y, n, i = nb.to('x y n i')
two        = nb.to(2)
sigma, pi  = nb.to('\\sigma \\pi')
L          = nb.symbol('{\\cal L}') # builds a formula from a latex expression
roman      = nb.rm('roman') # builds a formula using \mathrm
typed      = nb.tt('typed') # builds a formula using \texttt

# Then, basic operators can be used to combine formulas... let us
# illustrate some of them and put some results in the file basics.tex.


with nb.files.defs('001-001-basics.tex') as defs:
    nb.config.push('display style', True) # We set the displaystyle
    defs.prefix = 'ex'
    
    defs['CalL'] = L
    defs['Mathrm'] = roman
    defs['Texttt'] = typed

    defs['EqualA'] = L == roman # Makes an equality. You may encounter troubles with operand orders...
    defs['EqualB'] = nb.equal(L, roman) # ... so you can use this instead.
    # The same is available for comparison operators (nb.seq builds a sequence of expressions)
    defs['OpsA'] = nb.seq((x < y),     (x <= y),     (x != y),     (x >= y),     (x > y))
    defs['OpsB'] = nb.seq(nb.lt(x, y), nb.leq(x, y), nb.neq(x, y), nb.geq(x, y), nb.gt(x, y))
    
    nb.config.push('product', None) #default
    defs['ProdA'] = x*y
    
    nb.config.push('product', '.') 
    defs['ProdB'] = x*y
    nb.config.pop() # pop the last config setting.
    # nb.config.pop('product') pops the last 'product' config setting. Similar to pop() here.
    
    nb.config.push('product', 'x') 
    defs['ProdC'] = x*y
    nb.config.pop()
    
    e = 1 + sigma**2 / (-(x+y)**(x-y) + x*y)
    defs['Expr'] = e

    ee = 1 + sigma**2 // (-(x+y)**(x-y) + x*y)
    defs['FlatExpr'] = ee

    defs['Def'] = nb.define(L, e)
    
    defs['Approx'] = nb.approx(pi, 3.14)

    defs['Sequence'] = nb.seq(pi, x, ..., y, e, ...) # You can use ... !


    # Groups and tuples are made from lists... this may happen implicitely
    v = nb.to([n+1/n]) # explicit grouping formula from list.
    k = [n+1/n] ** n   # implicit grouping formula from list.
    defs['Group'] = nb.seq(v, k)
    
    # Nice attributes are available
    e = nb.to([x+y])
    defs['Decoration'] = nb.seq(e.bar, e.inv, e.T, e.star, e.plus, e.minus, e.prime)

    # nb.seq builds a formula that is a sequence of others.
    defs['IndexExponent'] = nb.seq(x*y, x^y, x**y, x@y, x@(y,sigma))    


    # nb.cat concatenates formulas, nb.kat does the same with spacing.
    defs['Cat'] = nb.cat(x**2, y**3, x**n)
    defs['Kat'] = nb.kat(x**2, y**3, x**n)


    # You can define functions.
    fname = nb.to('f')@(nb.seq(sigma, i), pi)
    f = nb.fun(fname)
    defs['Func'] = f(x, y, i, n, pi)

    xy = [x, y, i, 3] # a list, not a formula.
    xy_t = xy**nb.text('hello world') # a list combined with a formula makes a formula.
    defs['Text'] = xy_t
    

    # Layout arrange formulas as tabular. First is 'r', 'l', 'c' for
    # alignement, then the lines come.
    layout = nb.layout('c',
                       [n, n+1, n+2],
                       [x, x**2],
                       [pi],
                       [1, None, 3]) # None creates an empty slot.
    defs['Layout'] = layout
    
    # This generates a latex cheetsheet that you can compile and display.
    defs.add_preamble('\\usepackage{color}') # You can add lines in the cheetsheet preamble.
    defs.add_preamble('\\usepackage{listings}') 
    defs.cheatsheet() 

