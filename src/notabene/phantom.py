from . import basics

def vertical(*elem):
    phantom = basics.Formula([to(expr) for expr in exprs],
                             lambda args : '{\\vphantom{' + ''.join(['{' + str(arg) + '}' for arg in args]) + '}}')
    phantom = str(phantom)
    def phantomize(expr):
        return basics.Formula([to(expr)],
                              lambda args : '{' + str(args[0]) + phantom + '}');
    return phantomize
    

