from . import basics
from . import math

N   = basics.Symbol('\\mathbb{N}')
Z   = basics.Symbol('\\mathbb{Z}')
Q   = basics.Symbol('\\mathbb{Q}')
R   = basics.Symbol('\\mathbb{R}')
C   = basics.Symbol('\\mathbb{C}')
empty =  basics.Symbol('\\emptyset')


def range_cc(*elems):
    return basics.Formula(elems,
                          lambda args : '\\left[' + str(basics.Seq(*elems)) + '\\right]')

def range_co(*elems):
    return basics.Formula(elems,
                          lambda args : '\\left[' + str(basics.Seq(*elems)) + '\\right[')

def range_oc(*elems):
    return basics.Formula(elems,
                          lambda args : '\\left]' + str(basics.Seq(*elems)) + '\\right]')

def range_oo(*elems):
    return basics.Formula(elems,
                          lambda args : '\\left]' + str(basics.Seq(*elems)) + '\\right[')

def byext(*elems):
    return basics.Formula(elems,
                          lambda args : '\\left\\{' + str(basics.Seq(*elems)) + '\\right\\}')
def bydef(*elems):
    return basics.Formula(elems,
                          lambda args : '\\left\\{' + '\\; \\middle| \\; '.join([str(basics.to(arg)) for arg in args]) + '\\right\\}')

def singleton(elem):
    return byext(elem)

def isin(elem, the_set):
    return basics.InfixOp('\\in', elem, the_set)

def subset(elem, the_set):
    return basics.InfixOp('\\subset', elem, the_set)
    
def isnotin(elem, the_set):
    return basics.InfixOp('\\notin', elem, the_set)
    
def minus(set1, set2):
    return basics.InfixOp('\\setminus', set1, set2)
    
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

def Union(*args):
    return math.iteration('\\bigcup', args)

def Inter(*args):
    return math.iteration('\\bigcap', args)

def power(the_set):
    return basics.fun(basics.Symbol('{\\cal P}'))(the_set)

def functional(a, b):
    return b**a

def cartesian(*elems):
    return math.oplist('\\times', elems)

