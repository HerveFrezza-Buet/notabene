import notabene as nb

n = nb.to('n')

with nb.files.defs('notations.tex') as defs:
    nb.config.push('display style', True) # We set the displaystyle
    defs.prefix = 'ex'

    defs['Formula'] = nb.equal(nb.math.sum(n==0, nb.math.infinity, 1/n**2), nb.math.pi**2/6)
    
    # This generates a latex cheetsheet that you can compile and display.
    defs.cheatsheet() 


