import notabene as nb

mu, sigma, X, Y, Z, A, B, C = nb.to('\\mu \\sigma X Y Z A B C')


with nb.files.defs('probas.tex') as defs:
    nb.set_displaystyle(True)
    defs.prefix = 'ex'

    the_set = nb.sets.range_cc(0, 1)
    law1    = nb.proba.uniform(the_set)
    law2    = nb.proba.normal(mu, sigma)
    defs['Laws'] = nb.seq(law1, law2)

    defs['Proba'] = nb.seq(nb.proba.P(nb.sets.isin(X, A)),
                           nb.proba.P_cond(nb.sets.isin(X, A),
                                          nb.sets.isin(Y, B),
                                          nb.sets.isin(Z, C)))

    defs['CustomLaws'] = nb.seq(nb.proba.law(X),
                                nb.proba.law_cond(X,Y,Z))

    defs['Densities'] = nb.seq(nb.proba.density(X),
                               nb.proba.density_cond(X,Y,Z))

    defs['Follows'] = nb.proba.follows(X, law1)
    
    defs['Toss'] = nb.proba.toss_from('x', X)

    defs['Moments'] = nb.seq(nb.proba.expect(X),
                             nb.proba.var(X),
                             nb.proba.covar(X))

    defs.cheatsheet() 
