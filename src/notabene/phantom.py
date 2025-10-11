from . import basics

def vertical(*elems):
    phantom = basics.Formula([basics.to(expr) for expr in elems],
                             lambda args : '{\\vphantom{' + ''.join(['{' + str(arg) + '}' for arg in args]) + '}}')
    phantom = str(phantom)
    def phantomize(expr):
        return basics.Formula([basics.to(expr)],
                              lambda args : '{' + str(args[0]) + phantom + '}');
    return phantomize
    

