from . import basics

pi  = basics.Symbol('\\pi')
i   = basics.Symbol('\\mathrm{i}')
e   = basics.Symbol('\\mathrm{e}')
infinity = basics.Symbol('\\infty')

exp = basics.fun('\exp')

def oplist(opstring, operands):
    return basics.Formula([basics.to(op) for op in operands],
                          lambda args : (' {} '.format(opstring)).join(['{' + str(op) + '}' for op in operands]))

def iteration(symbol, args):
    if len(args) == 2:
        return basics.Formula([basics.to(symbol)]+[basics.to(arg) for arg in args],
                              lambda args : basics.insert_dsp() + str(args[0]) + '_{' + str(args[1]) + '}{' + str(args[2]) +'}')
    elif len(args) == 3:
        return basics.Formula([basics.to(symbol)]+[basics.to(arg) for arg in args],
                              lambda args : basics.insert_dsp() + str(args[0]) + '_{' + str(args[1]) + '}^{' + str(args[2]) +'}{' + str(args[3]) +'}')

def fact(expr):
    return basics.Formula([basics.to(expr)],
                          lambda args : str(args[0]) + '!')

def forall(expr1, expr2):
    return basics.Formula([basics.to(expr1), basics.to(expr2)],
                          lambda args : '\\forall ' + '{' + str(expr1) + '},\\; {' + str(expr2) +'}')

def exists(expr1, expr2):
    return basics.Formula([basics.to(expr1), basics.to(expr2)],
                          lambda args : '\\exists ' + '{' + str(expr1) + '},\\; {' + str(expr2) +'}')
    
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

def bracket(elem) : 
    return basics.Formula([elem],
                          lambda args : '\\left< ' + str(basics.to(args[0])) + ' \\right>')

def brace(elem) : 
    return basics.Formula([elem],
                          lambda args : '\\left\{ ' + str(basics.to(args[0])) + ' \\right\}')

def left_system(elem) : 
    return basics.Formula([elem],
                          lambda args : '\\left\{ ' + str(basics.to(args[0])) + ' \\right.')

def right_system(elem) : 
    return basics.Formula([elem],
                          lambda args : '\\left. ' + str(basics.to(args[0])) + ' \\right\}')

def sqrt(elem):
    return basics.Formula([elem],
                          lambda args : '\\sqrt{ ' + str(basics.to(args[0])) + '}')
    
