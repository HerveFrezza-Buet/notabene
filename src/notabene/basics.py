from . import config

def insert_dsp():
    if config.get('display style') :
        return '\\displaystyle'
    else:
        return ''

class Formula:
    def __init__(self, args, to_latex):
        self.args = args
        self.to_latex = to_latex
        self.max_argnum = 0
        for arg in args:
            if isinstance(arg, Formula) :
                self.max_argnum = max(self.max_argnum, arg.max_argnum)
        
    def __str__(self):
        return self.to_latex(self.args)

    def __getattr__(self, name):
        if name == 'T':
            return Exponent(self, Symbol('\\texttt{T}'))
        if name == 'inv':
            return Exponent(self, -1)
        if name == 'bar':
            return Overline(self)
        if name == 'hat':
            return Hat(self)
        if name == 'tilde':
            return Tilde(self)
        if name == 'at':
            return At(self)
        if name == 'star':
            return Exponent(self, Symbol('\\star'))
        if name == 'aster':
            return Exponent(self, Symbol('*'))
        if name == 'plus':
            return Exponent(self, Symbol('+'))
        if name == 'minus':
            return Exponent(self, Symbol('-'))
        if name == 'prime':
            return Exponent(self, Symbol('\\prime'))
        if name == 'dprime':
            return Exponent(self, Symbol('\\prime\\prime'))
        if name == 'trprime':
            return Exponent(self, Symbol('\\prime\\prime\\prime'))
        if name == 'dag':
            return Exponent(self, Symbol('\\dag'))
        if name == 'ddag':
            return Exponent(self, Symbol('\\ddag'))
        if name == 'ortho':
            return Exponent(self, Symbol('\\perp'))
        if name == '_ortho':
            return Index(self, Symbol('\\perp'))
        if name == 'para':
            return Exponent(self, Symbol('\\parallel'))
        if name == '_para':
            return Index(self, Symbol('\\parallel'))
        if name == 're':
            return re(self)
        if name == 'im':
            return im(self)
        if name == 'module':
            return module(self)
        if name == 'conj':
            return conj(self)
        if name == 'argument':
            return argument(self)
        else:
            raise AttributeError

    def isin(self, other):
        return InfixOp('\\in', self, other)
    
    def isnotin(self, other):
        return InfixOp('\\notin', self, other)
    
    def subset(self, other):
        return InfixOp('\\subset', self, other)

    def such_as(self, other):
        return seq(self, other)
    
    def equal(self, other):
        return equal(self, other)
    
    def equals(self, other):
        return equals(self, other)

    def lt(self, other):
        return lt(self, other)
    
    def leq(self, other):
        return leq(self, other)

    def neq(self, other):
        return neq(self, other)

    def gt(self, other):
        return gt(self, other)

    def geq(self, other):
        return geq(self, other)

    def approx(self, other):
        return approx(self, other)
    
    def add(self, other):
        return InfixOp('+', self, other)
    def __add__(self, other):
        return self.add(other)
    def __radd__(self, other):
        return to(other).add(self)
    
    def mul(self, other):
        select = {None : Cat(self, other),
                  '.' : InfixOp('{\\cdot}', self, other),
                  'x' : InfixOp('\\times', self, other)}
        return select[config.get('product')]
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
    
    def floordiv(self, other):
        return InfixOp('/', self, other)
    def __floordiv__(self, other):
        return self.floordiv(other)
    def __rfloordiv__(self, other):
        return to(other).floordiv(self)

    
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

def _format_float(expr):
    fmt = config.get('float')
    if isinstance(fmt, str):
        return eval("f'{expr:" + fmt + "}'")
    if isinstance(fmt, int):
        g_style = eval("f'{expr:." + str(fmt) + "g}'")
        exp = g_style.split('e')
        if len(exp) != 2:
            return str(''.join(exp))
        return exp[0] + '\\times 10^{' + exp[1].replace('+', '') + '}'
    return str(expr)

def to(expr):
    if isinstance(expr, type(None)):
        return Empty()
    if isinstance(expr, bool):
        if expr:
            return text('true')
        else:
            return text('false')
    if isinstance(expr, type(...)):
        return Symbol('\\ldots')
    if isinstance(expr, int):
        return Symbol(str(expr))
    if isinstance(expr, float):
        return Symbol(_format_float(expr))
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

def equal(*args):
    return InfixOp('=', *args)

def equals(*args):
    return equal(*args)

def lt(*args):
    return InfixOp('<', *args)
    
def leq(*args):
    return InfixOp('\\leq', *args)

def neq(*args):
    return InfixOp('\\neq', *args)

def gt(*args):
    return InfixOp('>', *args)

def geq(*args):
    return InfixOp('\\geq', *args)

def approx(*args):
    return InfixOp(Symbol('\\simeq'), *args)

def text(msg):
    return Formula([],
                   lambda args : '\\mbox{' + msg + '}')

def rm(msg):
    return Formula([to(msg)],
                   lambda args : '\\mathrm{' + str(args[0]) + '}')
def cal(msg):
    return Formula([to(msg)],
                   lambda args : '{\\cal ' + str(args[0]) + '}')
                   
def tt(msg):
    return Formula([to(msg)],
                   lambda args : '\\texttt{' + str(args[0]) + '}')
def bf(msg):
    return Formula([to(msg)],
                   lambda args : '\\textbf{' + str(args[0]) + '}')

def small(expr):
    return Formula([to(expr)],
                   lambda args : '{\\scriptstyle ' + str(expr) + '}')

def smaller(expr):
    return Formula([to(expr)],
                   lambda args : '{\\scriptscriptstyle ' + str(expr) + '}')

def arg(num):
    return Arg(num)


class Empty(Formula):
    def __init__(self):
        super().__init__([], lambda args : '{}' )
        
class Isolate(Formula):
    def __init__(self, expr):
        super().__init__([to(expr)], lambda args : '{' + str(args[0]) + '}')
        
class Arg(Formula):
    def __init__(self, num):
        super().__init__([], lambda args : '#' + str(num))
        self.max_argnum = num
        
class Overline(Formula):
    def __init__(self, expr):
        super().__init__([to(expr)], lambda args : '\\overline{' + str(args[0]) +'}')
        
class Hat(Formula):
    def __init__(self, expr):
        super().__init__([to(expr)], lambda args : '\\widehat{' + str(args[0]) +'}')
        
class Tilde(Formula):
    def __init__(self, expr):
        super().__init__([to(expr)], lambda args : '\\widetilde{' + str(args[0]) +'}')
    
class Seq(Formula):
    def __init__(self, *exprs):
        super().__init__([to(expr) for expr in exprs], lambda args : ',\\;'.join([str(arg) for arg in args]))

class Sek(Formula):
    def __init__(self, *exprs):
        super().__init__([to(expr) for expr in exprs], lambda args : ','.join([str(arg) for arg in args]))

def seq(*exprs):
    return Seq(*exprs)

def sek(*exprs):
    return Sek(*exprs)

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
                    lines_str.append(' & ' * (max_length - 1))
                elif max_length == 1:
                    lines_str.append(str(to(l[0])))
                else:
                    emptys = max_length - len(l)
                    line = ' & '.join([str(to(e)) for e in l[:-1]])
                    if emptys == 0:
                        line += ' & ' + str(to(l[-1]))
                    else:
                        if len(l) > 1:
                            line += ' & '
                        line += '\\multicolumn{' + str(emptys + 1) + '}{' + a + '}{' + str(to(l[-1])) + '}'
                    lines_str.append(line)
            res += ' \\\\ '.join(lines_str)
            res += ' \\end{array}'
            return res
        def list_of_line(l):
            if isinstance(l, list) :
                return l
            else:
                return [l]
        super().__init__([list_of_line(l) for l in lines],
                         lambda args : make_table(align, args))
    
def layout(*lines):
    return Layout(lines[0], lines[1:])


class Function:
    def __init__(self, name):
        self.name = to(name)

    def __call__(self, *exprs):
        return Formula([self.name] + [to(expr) for expr in exprs],
                       lambda args : '{' + str(args[0]) + '}\\!\\left(' + str(Seq(*(args[1:]))) + '\\right)')

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
    def __init__(self, op, *args):
        tos = [to(op)] + [to(arg) for arg in args]
        super().__init__(tos,
                         lambda args : str(args[0]).join(['{' + str(arg) + '}' for arg in args[1:]]))

class Pipe(Formula):
    def __init__(self, expr1, expr2):
        super().__init__([to(expr1), to(expr2)], lambda args : '\\left. {' + str(args[0]) + '}\\; \\middle|\\; {' + str(args[1]) + '}\\right.')
        
class At(Formula):
    def __init__(self, expr):
        super().__init__([to(expr)], lambda args : '\\left. {' + str(args[0]) + '}\\right|')

def pipe(expr1, expr2):
    return Pipe(expr1, expr2)

class Frac(Formula):
    def __init__(self, num, denom):
        super().__init__([to(num), to(denom)],
                         lambda args : insert_dsp() + '\\frac{' + str(args[0]) + '}{' + str(args[1]) + '}')


class Exponent(Formula):
    def __init__(self, expr, exponent):
        expr = to(expr)
        if isinstance(expr, Index):
            super().__init__([expr, to(exponent)],
                             lambda args : str(args[0]) + '^{' + str(args[1]) + '}')
        else:
            super().__init__([expr, to(exponent)],
                             lambda args : '{' + str(args[0]) + '}^{' + str(args[1]) + '}')
        
class Index(Formula):
    def __init__(self, expr, index):
        expr = to(expr)
        if isinstance(expr, Exponent):
            super().__init__([expr, to(index)],
                             lambda args : str(args[0]) + '_{' + str(args[1]) + '}')
        else:
            super().__init__([expr, to(index)],
                             lambda args : '{' + str(args[0]) + '}_{' + str(args[1]) + '}')
        
class IndexExp(Formula):
    def __init__(self, expr, index, exponent):
        super().__init__([to(expr), to(index), to(exponent)],
                         lambda args : '{' + str(args[0]) + '}_{' + str(args[1]) + '}^{' + str(args[2]) + '}')

def define(name, *expr):
    symb = Symbol('\\stackrel{\\mathrm{def}}{=}')
    defs = [name]
    for e in expr:
        defs += [symb, e]
    return kat(*defs)



def symbol(latex_expression):
    return Symbol(latex_expression)

def isolate(a):
    return Isolate(a)

### This is for complex numbers

def re(expr):
    return fun(rm('Re'))(expr)

def im(expr):
    return fun(rm('Im'))(expr)

def argument(expr):
    return fun(rm('arg'))(expr)

def module(expr):
    return fun(rm('mod'))(expr)

def conj(expr):
    mode = config.get('conjugate')
    if mode == '*':
        return expr.aster
    if mode == '_':
        return expr.bar
    raise ValueError(f"Bad conjugate mode ('{mode}') is currently used.")
                        
                         
