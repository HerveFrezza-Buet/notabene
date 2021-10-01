
class Formula:
    def __init__(self, args, to_latex):
        self.args = args
        self.to_latex = to_latex
        
    def __str__(self):
        return self.to_latex(self.args)
    
    def add(self, other):
        return InfixOp('+', self, other)
    def __add__(self, other):
        return self.add(other)
    def __radd__(self, other):
        return to(other).add(self)
    
    def mul(self, other):
        return Formula([self, to(other)], lambda args : '{{' + str(args[0]) + '}{' + str(args[1]) + '}}')
    def __mul__(self, other):
        return self.mul(other)
    def __rmul__(self, other):
        return to(other).mul(self)

    def matmul(self, other):
        return Index(self, other)
    def __matmul__(self, other):
        if(isinstance(other, tuple) or isinstance(other, list)):
            if(len(other) != 2):
                raise 'Expression {} cannot be used as an (index, exponent) pair.'.format(other)
            else:
                return IndexExp(self, other[0], other[1])
        else:
            return self.matmul(other)
    def __rmatmul__(self, other):
        return to(other).matmul(self)
    
    def times(self, other):
        return InfixOp('\\times', self, other)
    def __xor__(self, other):
        return self.times(other)
    def __rxor__(self, other):
        return to(other).times(self)
    
    def sub(self, other):
        return InfixOp('-', self, other)
    def __sub__(self, other):
        return self.sub(other)
    def __rsub__(self, other):
        return to(other).sub(self)
    
    def mod(self, other):
        return InfixOp('/', self, other)
    def __mod__(self, other):
        return self.mod(other)
    def __rmod__(self, other):
        return to(other).mod(self)
    
    def __neg__(self):
        return Formula([self], lambda args : '-{' + str(args[0]) + '}')
    
    def eq(self, other):
        return InfixOp('=', self, other)
    def __eq__(self, other):
        return self.eq(other)
    def __req__(self, other):
        return to(other).eq(self)
    
    def truediv(self, other):
        return Frac(self, other)
    def __truediv__(self, other):
        return self.truediv(other)
    def __rtruediv__(self, other):
        return to(other).truediv(self)
    
    def power(self, other):
        return Exponent(self, other)
    def __pow__(self, other):
        return self.power(other)
    def __rpow__(self, other):
        return to(other).power(self)

def to(expr):
    if isinstance(expr, int) or isinstance(expr, float):
        return Symbol(str(expr))
    if isinstance(expr, Formula):
        return expr
    if isinstance(expr, str):
        if len(expr.split()) != 1:
            raise 'String "{}" cannot be converted to a formula'.format(expr)
        else:
            return Symbol(str(expr))

class Seq(Formula):
    def __init__(self, *exprs):
        super().__init__([to(expr) for expr in exprs], lambda args : ','.join([str(arg) for arg in args]))

def seq(*exprs):
    return Seq(*exprs)

class Function:
    def __init__(self, name):
        self.name = to(name)

    def __call__(self, *exprs):
        return Formula([self.name] + [to(expr) for expr in exprs],
                       lambda args : '{' + str(args[0]) + '}\\left(' + str(Seq(*(args[1:]))) + '\\right)')

def fun(name):
    return Function(name)
                    

class Symbol(Formula):
    def __init__(self, latex_expression):
        super().__init__([], lambda x : latex_expression)

class InfixOp(Formula):
    def __init__(self, op, left, right):
        super().__init__([to(left), to(right), to(op)],
                         lambda args : '{' + str(left) + '} ' + str(op) + ' {' + str(right) + '}')

class Frac(Formula):
    def __init__(self, num, denom):
        super().__init__([to(num), to(denom)],
                         lambda args : '\\frac{' + str(num) + '}{' + str(denom) + '}')


class Exponent(Formula):
    def __init__(self, expr, exponent):
        super().__init__([to(expr), to(exponent)],
                         lambda args : '{' + str(expr) + '}^{' + str(exponent) + '}')
        
class Index(Formula):
    def __init__(self, expr, index):
        super().__init__([to(expr), to(index)],
                         lambda args : '{' + str(expr) + '}_{' + str(index) + '}')
        
class IndexExp(Formula):
    def __init__(self, expr, index, exponent):
        super().__init__([to(expr), to(index), to(exponent)],
                         lambda args : '{' + str(expr) + '}_{' + str(index) + '}^{' + str(exponent) + '}')
