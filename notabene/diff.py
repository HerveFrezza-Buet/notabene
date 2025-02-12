from . import basics
from . import math

def dn(n, *elem):
    dif = basics.Symbol('\\mathrm{d}')**basics.to(n)
    return basics.cat(*[basics.cat(dif, e) for e in elem])

def Dn(n, *elem):
    dif = basics.Symbol('\\partial')**basics.to(n)
    return basics.cat(*[basics.cat(dif, e) for e in elem])

def dfracn(n, *elem):
    return dn(n, elem[0]) / d(*(elem[1:]))**n

def Dfracn(n, *elem):
    return Dn(n, elem[0]) / D(*(elem[1:]))**n

def d(*elem):
    dif = basics.Symbol('\\mathrm{d}')
    return basics.cat(*[basics.cat(dif, e) for e in elem])

def D(*elem):
    dif = basics.Symbol('\\partial')
    return basics.cat(*[basics.cat(dif, e) for e in elem])

def dfrac(*elem):
    return d(elem[0]) / d(*(elem[1:]))

def Dfrac(*elem):
    return D(elem[0]) / D(*(elem[1:]))


def d2(*elem):
    return dn(2, *elem)

def D2(*elem):
    return Dn(2, *elem)

def dfrac2(*elem):
    return dfracn(2, *elem)

def Dfrac2(*elem):
    return Dfracn(2,*elem)





def dfun(*elem):
    return basics.fun(dfrac(*elem))

def Dfun(*elem):
    return basics.fun(Dfrac(*elem))

def G(elem, at=None):
    grad = basics.Symbol('\\nabla')
    if at:
        return basics.Formula([grad, basics.to(elem), basics.to(at)],
                              lambda args : '{\\left. {' + str(args[0]) + '}{' + str(args[1]) + '} \\right|}_{' + str(args[2]) + '}')
    else:
        return basics.cat(grad, elem)

def Gfun(elem, at=None):
    return basics.fun(G(elem, at))


def _integral(bounds):
    if isinstance(bounds, tuple):
        return basics.Formula([basics.to(bounds[0]), basics.to(bounds[1])],
                              lambda args : basics.insert_dsp() + '\\int_{' + str(args[0]) + '}^{' + str(args[1]) + '}')
    else:
        return basics.Formula([basics.to(bounds)],
                              lambda args : basics.insert_dsp() + '\\int_{' + str(args[0]) + '}')
                              
def integral(ints, expr, diffs):
    if isinstance(ints, list):
        integrals = ints
    else:
        integrals = [ints]
    line = [_integral(i) for i in integrals]
    if integrals[-1] == None:
        line.append(basics.Symbol('\\,'))
    line.append(basics.to(expr))
    if isinstance(diffs, list):
        line.append(d(*diffs))
    else:
        line.append(d(diffs))
    return basics.cat(*line)

