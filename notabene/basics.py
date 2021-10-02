displaystyle = False

def set_displaystyle(value):
    global displaystyle
    displaystyle = value

def insert_dsp():
    if displaystyle :
        return '\\displaystyle'
    else:
        return ''

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
    
    def __pos__(self):
        return Formula([self], lambda args : '+{' + str(args[0]) + '}')
    
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
    
    def __lt__(self, other):
        return InfixOp('<', self, other)
    
    def __le__(self, other):
        return InfixOp('\\leq', self, other)
    
    def __eq__(self, other):
        return InfixOp('=', self, other)

    def __ne__(self, other):
        return InfixOp('\\neq', self, other)
    
    def __gt__(self, other):
        return InfixOp('>', self, other)
    
    def __ge__(self, other):
        return InfixOp('\\geq', self, other)
    

def to(expr):
    if isinstance(expr, type(...)):
        return Symbol('\\ldots')
    if isinstance(expr, int) or isinstance(expr, float):
        return Symbol(str(expr))
    if isinstance(expr, Formula):
        return expr
    if isinstance(expr, str):
        l = expr.split()
        if len(l) != 1:
            return [to(e) for e in l]
        else:
            return Symbol(str(expr))
    if isinstance(expr, list):
        return Formula([to(e) for e in expr],
                       lambda args : '\\left(' + ','.join([str(arg) for arg in args]) + '\\right)')

def text(msg):
    return Formula([msg],
                   lambda args : '\\mbox{' + msg + '}')
class Seq(Formula):
    def __init__(self, *exprs):
        super().__init__([to(expr) for expr in exprs], lambda args : ','.join([str(arg) for arg in args]))

def seq(*exprs):
    return Seq(*exprs)

class Cat(Formula):
    def __init__(self, *exprs):
        super().__init__([to(expr) for expr in exprs], lambda args : ''.join(['{' + str(arg) + '}' for arg in args]))

def cat(*exprs):
    return Cat(*exprs)

class Kat(Formula):
    def __init__(self, *exprs):
        super().__init__([to(expr) for expr in exprs], lambda args : '\\;'.join(['{' + str(arg) + '}' for arg in args]))

def kat(*exprs):
    return Kat(*exprs)

class Layout(Formula):
    def __init__(self, align, lines):
        def make_table(a, ls):
            max_length = max([len(l) for l in ls])
            res = '\\begin{array}{' + a*max_length + '} '
            lines_str = []
            for l in ls:
                if len(l) == 0:
                    lines_str.append(' & ' * max_length)
                else:
                    emptys = max_length - len(l)
                    line = ' & '.join([str(to(e)) for e in l[:-1]])
                    if emptys == 0:
                        line += ' & ' + str(to(l[-1]))
                    else:
                        if len(l) > 1:
                            line += ' & '
                        line += '\multicolumn{' + str(emptys + 1) + '}{' + a + '}{' + str(to(l[-1])) + '}'
                    lines_str.append(line)
            res += ' \\\\ '.join(lines_str)
            res += ' \\end{array}'
            return res
        super().__init__(lines,
                         lambda args : make_table(align, args))
    
def layout(*lines):
    return Layout(lines[0], lines[1:])


class Function:
    def __init__(self, name):
        self.name = to(name)

    def __call__(self, *exprs):
        return Formula([self.name] + [to(expr) for expr in exprs],
                       lambda args : '{' + str(args[0]) + '}\\left(' + str(Seq(*(args[1:]))) + '\\right)')

def fun(name):
    if isinstance(name, str):
        names = name.split()
        if len(names) > 1:
            return [fun(e) for e in names]
        else:
            return Function(name)
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
                         lambda args : insert_dsp() + '\\frac{' + str(num) + '}{' + str(denom) + '}')


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
