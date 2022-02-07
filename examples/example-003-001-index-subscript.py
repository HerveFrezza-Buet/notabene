import notabene as nb


with nb.files.defs('003-001-index-subscript.tex') as defs:
    nb.config.push('display style', True) # We set the displaystyle
    defs.prefix = 'ex'

    x = nb.to('x')

    # The basic indexing is
    i = x@2

    # The basic exponent is
    e = x**3

    # The basic "both" is
    b = x@(2,3)

    defs['Basic'] = nb.seq(i, e, b)

    # Indexation is clever
    defs['Indexation'] = nb.seq(i@5, e@5, b@5)
    
    # Exponentiation is clever
    defs['Exponentiation'] = nb.seq(i**7, e**7, b**7)
    
    # Both is clever
    defs['Both'] = nb.seq(i@(5, 7), e@(5, 7), b@(5, 7))

    # You can remove the clever handling of indexes/exponents by isolating your formula.

    i = nb.isolate(i)
    e = nb.isolate(e)
    defs['Isolate'] = nb.seq(e@5, i**7)

    
    defs.cheatsheet() 

