from . import basics
from . import math


def conj(*elems):
    return math.oplist('\\wedge', elems)

def disj(*elems):
    return math.oplist('\\vee', elems)

def imply(*elems):
    return math.oplist('\\Rightarrow', elems)

def equiv(*elems):
    return math.oplist('\\Leftrightarrow', elems)

def neg(expr):
    return basics.cat(basics.Symbol('\\neg'), expr)
