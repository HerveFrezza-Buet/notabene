import notabene as nb

A, B, C = nb.to('A B C')
a, b    = nb.to('a b')


with nb.files.defs('linalg.tex') as defs:
    nb.set_displaystyle(True)
    defs.prefix = 'ex'

    defs['Basics'] = nb.seq(A.T, A.inv, A.plus, nb.linalg.det(A), nb.linalg.trace(A))

    nb.set_vector_mode(None) # default 
    x, y, z  = nb.linalg.vec('x y z')
    defs['VecNone'] = nb.seq(x, y, z, nb.linalg.vec(a+b))
    
    nb.set_vector_mode('bold')
    xb, yb, zb  = nb.linalg.vec('x y z')
    defs['VecBold'] = nb.seq(xb, yb, zb, nb.linalg.vec(a+b))
    
    nb.set_vector_mode('->')
    xa, ya, za  = nb.linalg.vec('x y z')
    defs['VecArrow'] = nb.seq(xa, ya, za, nb.linalg.vec(a+b))
    
    nb.set_vector_mode(None)

    nb.set_dot_product_mode(None) # default
    dot1 = nb.linalg.dot(xb, ya)
    
    nb.set_dot_product_mode('.')
    dot2 = nb.linalg.dot(xb, ya)
    
    nb.set_dot_product_mode('<|>')
    dot3 = nb.linalg.dot(xb, ya)
    
    nb.set_dot_product_mode('T') # Let is keep this
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
    

    
    defs.cheatsheet() 
