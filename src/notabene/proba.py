from . import config
from . import basics
from . import math

_Esymb = basics.Symbol('\\mathrm{E}')
_Psymb = basics.Symbol('\\mathrm{P}')
_Dsymb = basics.Symbol('\\mathrm{p}')


def _cond(*elems):
    if config.get('proba cond') == '_':
        return basics.Formula([basics.to(e) for e in elems],
                              lambda args : '{' + str(args[0]) + '}_{''\\left| ' + str(basics.seq(*(args[1:]))) + '\\right.}')
    else:
        return basics.Formula([basics.to(e) for e in elems],
                              lambda args : '\\left. {'+ str(args[0]) + '}\\; \\middle|\\; ' + str(basics.seq(*(args[1:]))) + '\\right.')
    

def cond(*variables):
    return _cond(*variables)

def uniform(the_set):
    return basics.Symbol('{\\cal U}')@the_set

def normal(mu, sigma):
    return basics.fun(basics.Symbol('{\\cal N}'))(mu, sigma)

def bernouilli(p):
    return basics.fun(basics.Symbol('{\\cal B}'))(p)

def joint(*elems):
    return basics.cat(*elems)

def P(event):
    return basics.fun(_Psymb)(event)

def P_cond(*elems):
    return basics.fun(_Psymb)(_cond(*elems))

def law(var):
    return _Psymb@var

def law_cond(*variables):
    return _Psymb@_cond(*variables)

def density(var):
    return _Dsymb@var

def density_cond(*variables):
    return _Dsymb@_cond(*variables)

def follows(var, law):
    return basics.InfixOp('\\sim', var, law)

def toss_from(sample, var):
    return basics.InfixOp('\\dashleftarrow', sample, var)

def expect(var):
    return basics.Formula([basics.to(var)],
                          lambda args : str(_Esymb) + '\\left[' + str(args[0]) + '\\right]')

def var(v):
    return basics.fun(basics.Symbol('\\mathrm{var}'))(v)

def covar(v):
    return basics.fun(basics.Symbol('\\mathrm{cov}'))(v)
