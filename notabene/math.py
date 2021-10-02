from . import basics

pi  = basics.Symbol('\\pi')
i   = basics.Symbol('\\mathrm{i}')
e   = basics.Symbol('\\mathrm{e}')
infinity = basics.Symbol('\\infty')

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
