from . import basics
from . import math

N   = basics.Symbol('\\mathbb{N}')
Z   = basics.Symbol('\\mathbb{Z}')
Q   = basics.Symbol('\\mathbb{Q}')
R   = basics.Symbol('\\mathbb{R}')
C   = basics.Symbol('\\mathbb{C}')


def byext(*elems):
    return basics.Formula(elems,
                          lambda args : '\\left\\{' + str(basics.Seq(*elems)) + '\\right\\}')
def bydef(*elems):
    return basics.Formula(elems,
                          lambda args : '\\left\\{' + '\\; \\middle| \\; '.join([str(basics.to(arg)) for arg in args]) + '\\right\\}')

def isin(elem, the_set):
    return basics.Formula([elem, the_set],
                          lambda args : str(basics.to(args[0])) + '\\in' + str(basics.to(args[1])))
def isnotin(elem, the_set):
    return basics.Formula([elem, the_set],
                          lambda args : str(basics.to(args[0])) + '\\notin' + str(basics.to(args[1])))
def indic(the_set):
    return basics.fun(basics.Symbol('\\mathbb{1}')@basics.to(the_set))

def min(who, what):
    return math.iteration('\\mathop{\\mathrm{min}}', [who, what])

def max(who, what):
    return math.iteration('\\mathop{\\mathrm{max}}', [who, what])

def argmin(who, what):
    return math.iteration('\\mathop{\\mathrm{argmin}}', [who, what])

def argmax(who, what):
    return math.iteration('\\mathop{\\mathrm{argmax}}', [who, what])

def union(*elems):
    return math.oplist('\\cup', elems)

def inter(*elems):
    return math.oplist('\\cap', elems)
