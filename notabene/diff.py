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

