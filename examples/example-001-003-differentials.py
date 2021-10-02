import notabene as nb

x, y, z, i, n = nb.to('x y z i n')
f, g, h       = nb.fun('f g h')

with nb.files.defs('diff.tex') as defs:
    nb.set_displaystyle(True)
    defs.prefix = 'ex'

    defs['D'] = nb.seq(nb.diff.d(x,y,z),
                       nb.diff.D(x,y,z))
    
    defs['DFrac'] = nb.seq(nb.diff.dfrac(x,y,z),
                           nb.diff.Dfrac(x,y,z))

    f1 = nb.diff.dfun(x, y, z)
    f2 = nb.diff.Dfun(x, y, z)
    defs['DFun'] = nb.seq(f1(i**n), f2(i**n))
    

    defs.cheatsheet() 
