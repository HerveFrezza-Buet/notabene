import notabene as nb

mu, sigma, p, X, Y, Z, A, B, C = nb.to('\\mu \\sigma p X Y Z A B C')


with nb.files.defs('001-006-probas.tex') as defs:
    nb.config.push('display style', True) 
    defs.prefix = 'ex'

    the_set = nb.sets.range_cc(0, 1)
    law1    = nb.proba.uniform(the_set)
    law2    = nb.proba.normal(mu, sigma)
    law3    = nb.proba.bernouilli(p)

    ABC = nb.proba.joint(A, B, C)
    A_BC = nb.proba.cond(A, B, C)
    
    defs['Laws'] = nb.seq(law1, law2, law3)

    defs['Proba'] = nb.seq(nb.proba.P(nb.sets.isin(X, A)),
                           nb.proba.P_cond(nb.sets.isin(X, A),
                                          nb.sets.isin(Y, B),
                                          nb.sets.isin(Z, C)))


    defs['Joint'] = ABC
    defs['Cond'] = A_BC

    defs['CustomLaws'] = nb.seq(nb.proba.law(X),
                                nb.proba.law_cond(X,Y,Z))

    defs['Densities'] = nb.seq(nb.proba.density(X),
                               nb.proba.density_cond(X,Y,Z))

    defs['DensitiesOf'] = nb.equals(nb.fun(nb.proba.density(nb.proba.joint(X,Y)))('x', 'y'),
                                    nb.fun(nb.proba.density_cond(Y, X == 'x'))('y') * nb.fun(nb.proba.density(X))('x'))

    # You can trigger subscript mode for conditional probabilities
    nb.config.push('proba cond', '_')
    defs['SubscriptCond'] = nb.seq(nb.proba.cond(A, B, C),
                                   nb.proba.law_cond(X,Y,Z),
                                   nb.proba.density_cond(X,Y,Z))
    nb.config.pop()

    defs['Follows'] = nb.proba.follows(X, law1)
    
    defs['Toss'] = nb.proba.toss_from('x', X)

    defs['Moments'] = nb.seq(nb.proba.expect(X),
                             nb.proba.var(X),
                             nb.proba.covar(X))

    defs.cheatsheet() 
