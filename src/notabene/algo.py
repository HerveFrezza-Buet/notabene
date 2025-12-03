from . import basics


def affect(a, b):
    return basics.InfixOp(basics.Symbol('\\leftarrow'), a, b)

def iadd(a, b):
    return basics.InfixOp(basics.Symbol('\\mathrel{+}='), a, b)

def isub(a, b):
    return basics.InfixOp(basics.Symbol('\\mathrel{-}='), a, b)

def imul(a, b):
    return basics.InfixOp(basics.Symbol('\\mathrel{\\times}='), a, b)

def idiv(a, b):
    return basics.InfixOp(basics.Symbol('\\mathrel{/}='), a, b)
