import notabene as nb
from notabene.linalg import bra, ket # enable ket(x) instead of nb.linalg.ket(x)

A, B, C = nb.to('A B C')
a, b    = nb.to('a b')


with nb.files.defs('001-007-linalg.tex') as defs:
    nb.config.push('display style', True)
    defs.prefix = 'ex'

    defs['Basics'] = nb.seq(A.T, A.inv, A.plus, nb.linalg.det(A), nb.linalg.trace(A))

    nb.config.push('vector', None) # default 
    x, y, z  = nb.linalg.vec('x y z')
    defs['VecNone'] = nb.seq(x, y, z, nb.linalg.vec(a+b))
    nb.config.pop('vector') # Could have been nb.config.pop()
    
    nb.config.push('vector', 'bold') 
    xb, yb, zb  = nb.linalg.vec('x y z')
    defs['VecBold'] = nb.seq(xb, yb, zb, nb.linalg.vec(a+b))
    nb.config.pop()
    
    nb.config.push('vector', '->') 
    xa, ya, za  = nb.linalg.vec('x y z')
    defs['VecArrow'] = nb.seq(xa, ya, za, nb.linalg.vec(a+b))
    nb.config.pop()
    

    nb.config.push('dot product', None) # default 
    dot1 = nb.linalg.dot(xb, ya)
    nb.config.pop('dot product') # Could have been nb.config.pop()
    
    nb.config.push('dot product', '.') 
    dot2 = nb.linalg.dot(xb, ya)
    nb.config.pop()
    
    nb.config.push('dot product', '<|>')
    dot3 = nb.linalg.dot(xb, ya)
    nb.config.pop()
    
    nb.config.push('dot product', 'T') # Let us keep this (we do not pop yet)
    dot4 = nb.linalg.dot(xb, ya)

    defs['DotProducts'] = nb.seq(dot1, dot2, dot3, dot4)

    param = nb.linalg.vec('\\theta')
    phi   = nb.fun('\\varphi')
    defs['Linear'] = nb.linalg.dot(param, phi(x)) + b

    a, b, c, d, x, y = nb.to('a b c d x y')
    M = nb.linalg.matrix([a, b],
                         [c, d])
    X = nb.linalg.matrix(x,
                         y)
    Y = nb.linalg.matrix(a*x + b*y,
                         c*x + d*y)
    defs['Matrix'] = M * X == Y
    defs['Dots'] = nb.seq(nb.linalg.matrix([1,            nb.dots('_'),  0           ],
                                           [nb.dots('|'), nb.dots('\\'), nb.dots('|')],
                                           [0,            nb.dots('_'),  0           ]),
                          nb.linalg.matrix([0,            nb.dots('_'),  1           ],
                                           [nb.dots('|'), nb.dots('/'),  nb.dots('|')],
                                           [1,            nb.dots('_'),  0           ]))

    nb.config.pop()
    nb.config.push('dot product', '<|>')
    nb.config.push('product', None)
    phi, psi = nb.to('\\varphi \\psi')
    
    defs['MecaQ'] = nb.seq(nb.linalg.dot(phi, psi), bra(phi), ket(psi), bra(phi)*ket(psi),  bra(phi)*'A'*ket(psi))
    

    
    defs.cheatsheet() 
