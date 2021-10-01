from . import basics

pi  = basics.Symbol('\\pi')
i   = basics.Symbol('\\mathrm{i}')
e   = basics.Symbol('\\mathrm{e}')
infinity = basics.Symbol('\\infty')

N   = basics.Symbol('\\mathbb{N}')
Z   = basics.Symbol('\\mathbb{Z}')
Q   = basics.Symbol('\\mathbb{Q}')
R   = basics.Symbol('\\mathbb{R}')
C   = basics.Symbol('\\mathbb{C}')

exp = basics.fun('\exp')

def iteration(symbol, args):
    if len(args) == 2:
        return basics.Formula([basics.to(symbol)]+[basics.to(arg) for arg in args],
                              lambda args : str(args[0]) + '_{' + str(args[1]) + '}{' + str(args[2]) +'}')
    elif len(args) == 3:
        return basics.Formula([basics.to(symbol)]+[basics.to(arg) for arg in args],
                              lambda args : str(args[0]) + '_{' + str(args[1]) + '}^{' + str(args[2]) +'}{' + str(args[3]) +'}')

def fact(expr):
    return basics.Formula([basics.to(expr)],
                          lambda args : str(args[0]) + '!')

def sum(*args):
    return iteration('\\sum', args)

def prod(*args):
    return iteration('\\prod', args)

def min(who, what):
    return iteration('\\mathop{\\mathrm{min}}', [who, what])

def max(who, what):
    return iteration('\\mathop{\\mathrm{max}}', [who, what])

def argmin(who, what):
    return iteration('\\mathop{\\mathrm{argmin}}', [who, what])

def argmax(who, what):
    return iteration('\\mathop{\\mathrm{argmax}}', [who, what])

def set_ext(*elems):
    return basics.Formula(elems,
                          lambda args : '\\left\\{' + str(basics.Seq(*elems)) + '\\right\\}')
def set_def(*elems):
    return basics.Formula(elems,
                          lambda args : '\\left\\{' + ' \\middle| '.join([str(basics.to(arg)) for arg in args]) + '\\right\\}')
def belongs(elem, the_set):
    return basics.Formula([elem, the_set],
                          lambda args : str(basics.to(args[0])) + '\in' + str(basics.to(args[1])))

def indic(the_set):
    return basics.fun(basics.Symbol('\\mathbb{1}')@basics.to(the_set))

def abs(elem) : 
    return basics.Formula([elem],
                          lambda args : '\\left| ' + str(basics.to(args[0])) + ' \\right|')

def norm(elem) : 
    return basics.Formula([elem],
                          lambda args : '\\left\\| ' + str(basics.to(args[0])) + ' \\right\\|')

def matrix(elem) : 
    return basics.Formula([elem],
                          lambda args : '\\left[ ' + str(basics.to(args[0])) + ' \\right]')

def left_system(elem) : 
    return basics.Formula([elem],
                          lambda args : '\\left\{ ' + str(basics.to(args[0])) + ' \\right.')

def right_system(elem) : 
    return basics.Formula([elem],
                          lambda args : '\\left. ' + str(basics.to(args[0])) + ' \\right\}')
