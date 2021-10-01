from . import basics

pi  = basics.Symbol('\\pi')
i   = basics.Symbol('\\mathrm{i}')
e   = basics.Symbol('\\mathrm{e}')

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

def sum(*args):
    return iteration('\\sum', args)

def prod(*args):
    return iteration('\\prod', args)

def integral(*args):
    return iteration('\\int', args)

def min(who, what):
    return iteration('\\mathop{\\mathrm{min}}', *[who, what])

def max(who, what):
    return iteration('\\mathop{\\mathrm{max}}', *[who, what])

def argmin(who, what):
    return iteration('\\mathop{\\mathrm{argmin}}', *[who, what])

def argmax(who, what):
    return iteration('\\mathop{\\mathrm{argmax}}', *[who, what])

def set(*elems):
    return basics.Formula(elems,
                          lambda args : '\\left{' + str(Seq(*elems)) + '\\right}')
