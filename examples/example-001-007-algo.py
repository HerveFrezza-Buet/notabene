import notabene as nb


i = nb.to('i')
with nb.files.defs('algo.tex') as defs:
    nb.config.push('display style', True)
    defs.prefix = 'ex'

    defs['Affect'] = nb.algo.affect(i, i+1)
    
    defs.cheatsheet() 
