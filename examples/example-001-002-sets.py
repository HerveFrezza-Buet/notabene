import notabene as nb

x, y, z, i, n = nb.to('x y z i n')
f, g, h       = nb.fun('f g h')

with nb.files.defs('sets.tex') as defs:
    nb.set_displaystyle(True)
    defs.prefix = 'ex'

    defs['Empty'] = nb.sets.empty
    defs['IsIn'] = nb.sets.isin(x, nb.sets.Z)
    defs['IsNotIn'] = nb.sets.isnotin(x, nb.sets.C)
    defs['Subset'] = nb.sets.subset(x, nb.sets.C)
    defs['Minus'] = nb.sets.minus(nb.sets.C, nb.sets.singleton(x))
    
    A = nb.sets.byext(1, 2, ..., n)
    B = nb.sets.bydef(nb.sets.isin(x, nb.sets.Q), f(x+3) > 38)
    
    defs['ByExt'] = 'A' == A         # Equality is reversed.
    defs['ByDef'] = nb.to('B') == B  # Order is ok.
    defs['Ranges'] = nb.seq(nb.sets.range_cc(x, y, z),
                            nb.sets.range_co(x, y, z),
                            nb.sets.range_oc(x, y, z),
                            nb.sets.range_oo(x, y, z))
    defs['PowerSet'] = nb.sets.power(nb.sets.R)
    defs['Functional'] = nb.sets.functional(nb.to('A'), nb.to('B'))
    defs['Cartesian'] = nb.sets.isin([x, y, z],
                                     nb.sets.cartesian(nb.to('A'), nb.to('B'), nb.sets.Q))

    indic_b = nb.sets.indic(B)
    defs['Indic'] = indic_b(y)
    
    where = nb.sets.isin(y, B)
    what = nb.fun('g')(y**2)
    defs['Max']    = nb.sets.max(where, what)
    defs['Min']    = nb.sets.min(where, what)
    defs['Argmax'] = nb.sets.argmax(where, what)
    defs['Argmin'] = nb.sets.argmin(where, what)

    defs['Union'] = nb.sets.union(x,y,z)
    defs['Inter'] = nb.sets.inter(x,y,z)

    defs['UnionIter'] = nb.seq(nb.sets.Union(i==1, n, x@i),
                               nb.sets.Union(nb.sets.subset(i,x), i)) 
    defs['InterIter'] = nb.seq(nb.sets.Inter(i==1, n, x@i),
                               nb.sets.Inter(nb.sets.subset(i,x), i)) 
    
    defs.cheatsheet() 
