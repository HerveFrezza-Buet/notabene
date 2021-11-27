import notabene as nb


i = nb.to('i')
with nb.files.defs('001-008-algo.tex') as defs:
    nb.config.push('display style', True)
    defs.prefix = 'ex'

    defs['Affect'] = nb.algo.affect(i, i+1)
    
    defs.cheatsheet() 
