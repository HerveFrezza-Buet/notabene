from . import basics


def affect(a, b):
    return basics.InfixOp(basics.Symbol('\\leftarrow'), a, b)
