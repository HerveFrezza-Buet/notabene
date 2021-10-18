from . import basics
from . import math

vector_mode = None

def set_vector_mode(value):
    global vector_mode
    vector_mode = value
    
dot_product_mode = None

def set_dot_product_mode(value):
    global dot_product_mode
    dot_product_mode = value

def __vec_of(expr):
    select = {None   :  expr,
              '->'   : basics.Formula([expr], lambda args : '\\vv{' + str(args[0]) + '}'),
              'bold' : basics.Formula([expr], lambda args : '\mathbf{' + str(args[0]) + '}')}
    return select[vector_mode]

def vec(expr):
    formulas = basics.to(expr)
    if isinstance(formulas, list) :
        return [__vec_of(f) for f in formulas]
    else:
        return __vec_of(formulas)
    
def dot(a, b):
    a, b = basics.to(a), basics.to(b)
    select = {None   : basics.Cat(a, b),
              '.'    : basics.InfixOp('.', a, b),
              'T'    : a.T * b,
              '<|>'  : basics.Formula([a, b],
                                      lambda args : '\\left< {' + str(args[0]) + '} \\middle| {' + str(args[1]) + '} \\right>')}
    return select[dot_product_mode]

def det(a):
    return basics.fun(basics.Symbol('\\mathrm{det}'))(a)

def trace(a):
    return basics.fun(basics.Symbol('\\mathrm{Tr}'))(a)
    
def matrix(*lines):
    return math.matrix(basics.layout(*(['c'] + list(lines))))

def dots(kind) : 
    select = {'|'  : basics.Symbol('\\vdots'),
              '_'  : basics.Symbol('\\cdots'),
              '/'  : basics.Symbol('\\iddots'),
              '\\' : basics.Symbol('\\ddots')}
    return select[kind]
