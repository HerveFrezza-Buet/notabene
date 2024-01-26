from . import basics
from . import math

_Esymb = basics.Symbol('\\mathrm{E}')
_Psymb = basics.Symbol('\\mathrm{P}')
_Dsymb = basics.Symbol('\\mathrm{p}')

def _cond_parentheses(*elems):
    return basics.Formula([basics.to(e) for e in elems],
                          lambda args : '\\left( {'+ str(args[0]) + '}\\; \\middle|\\; ' + str(basics.seq(*(args[1:]))) + '\\right)')

def _cond_none(*elems):
    return basics.Formula([basics.to(e) for e in elems],
                          lambda args : '\\left. {'+ str(args[0]) + '}\\; \\middle|\\; ' + str(basics.seq(*(args[1:]))) + '\\right.')
    

def uniform(the_set):
    return basics.Symbol('{\\cal U}')@the_set

def normal(mu, sigma):
    return basics.fun(basics.Symbol('{\\cal N}'))(mu, sigma)

def joint(*elems):
    return basics.cat(*elems)

def P(event):
    return basics.fun(_Psymb)(event)

def P_cond(*elems):
    return basics.cat(_Psymb, _cond_parentheses(*elems))

def law(var):
    return _Psymb@var

def law_cond(*variables):
    return _Psymb@_cond_none(*variables)

def density(var):
    return _Dsymb@var

def density_cond(*variables):
    return _Dsymb@_cond_none(*variables)

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
