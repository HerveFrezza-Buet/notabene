import notabene as nb

x, y, z, i, n = nb.to('x y z i n')
f, g, h       = nb.fun('f g h')

with nb.files.defs('sets.tex') as defs:
    nb.set_displaystyle(True)
    defs.prefix = 'ex'

    defs['IsIn'] = nb.sets.isin(x, nb.sets.Z)
    defs['IsNotIn'] = nb.sets.isnotin(x, nb.sets.C)
    
    A = nb.sets.byext(1, 2, ..., n)
    B = nb.sets.bydef(nb.sets.isin(x, nb.sets.Q), f(x+3) > 38)
    
    defs['ByExt'] = 'A' == A         # Equality is reversed.
    defs['ByDef'] = nb.to('B') == B  # Order is ok.

    indic_b = nb.sets.indic(B)
    defs['Indic'] = indic_b(y)
    
    where = nb.sets.isin(y, B)
    what = nb.fun('g')(y**2)
    defs['Max']    = (nb.sets.max(where, what))
    defs['Min']    = (nb.sets.min(where, what))
    defs['Argmax'] = (nb.sets.argmax(where, what))
    defs['Argmin'] = (nb.sets.argmin(where, what))
    

    defs.cheatsheet() 
