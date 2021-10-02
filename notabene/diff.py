from . import basics
from . import math

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

def dfun(*elem):
    return basics.fun(dfrac(*elem))

def Dfun(*elem):
    return basics.fun(Dfrac(*elem))

def G(elem):
    grad = basics.Symbol('\\nabla')
    return basics.cat(grad, elem)

def Gfun(*elem):
    return basics.fun(G(*elem))


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
    line.append(basics.to(expr))
    if isinstance(diffs, list):
        line.append(d(*diffs))
    else:
        line.append(d(diffs))
    return basics.cat(*line)

