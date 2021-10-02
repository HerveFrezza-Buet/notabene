import notabene as nb

A, B, C = nb.to('A B C')


with nb.files.defs('logical.tex') as defs:
    defs.prefix = 'ex'

    defs['And'] = nb.logical.conj(A, B, C)
    defs['Or'] = nb.logical.disj(A, B, C)
    defs['Imply'] = nb.logical.imply(A, B, C)
    defs['Equiv'] = nb.logical.equiv(A, B, C)
    defs['Not'] = nb.logical.neg(A)
    defs['Definition'] = nb.define(nb.logical.imply(A, B), nb.logical.disj(nb.logical.neg(A), B))
    
    defs.cheatsheet() 
