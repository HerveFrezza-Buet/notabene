import notabene as nb

x, y, z, i, n = nb.to('x y z i n')
f, g, h       = nb.fun('f g h')

with nb.files.defs('001-003-sets.tex') as defs:
    nb.config.push('display style', True)
    defs.prefix = 'ex'

    defs['Constants'] = nb.seq(nb.sets.empty, nb.sets.N, nb.sets.Z, nb.sets.Q, nb.sets.R, nb.sets.C, nb.sets.Boolean)
    defs['IsIn'] = nb.sets.isin(x, nb.sets.Z)
    defs['IsNotIn'] = nb.sets.isnotin(x, nb.sets.C)
    defs['Subset'] = nb.sets.subset(x, nb.sets.C)
    defs['Minus'] = nb.sets.minus(nb.sets.C, nb.sets.singleton(x))
    
    A = nb.sets.byext(1, 2, ..., n)
    B = nb.sets.bydef(nb.sets.isin(x, nb.sets.Q), f(x+3) > 38, x <= 2)
    
    defs['ByExtA'] = 'A' == A         # Equality is reversed.
    defs['ByExtB'] = nb.equal('A', A) # Order is made OK
    defs['ByDef'] = nb.to('B') == B   # Order is ok.
    defs['Ranges'] = nb.seq(nb.sets.range_cc(x, y, z),
                            nb.sets.range_co(x, y, z),
                            nb.sets.range_oc(x, y, z),
                            nb.sets.range_oo(x, y, z))
    defs['PowerSet'] = nb.sets.power(nb.sets.R)
    defs['Functional'] = nb.sets.functional(nb.to('A'), nb.to('B'))
    defs['Cartesian'] = nb.sets.isin([x, y, z],
                                     nb.sets.cartesian(nb.to('A'), nb.to('B'), nb.sets.Q))
    defs['Cardinal'] = nb.sets.card(nb.sets.empty) == 0

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
