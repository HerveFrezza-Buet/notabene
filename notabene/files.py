
from . import basics
from pathlib import Path

class defs:
    def __init__(self, path):
        if isinstance(path, Path):
            self.path = path
        else:
            self.path = Path(path)
        self.prefix = None
        self.content = []

    
    def __setitem__(self, at, value):
        if self.prefix:
            key = '{}{}'.format(self.prefix, at)
        else:
            key = at
        expr = str(basics.to(value))
        command = '\\newcommand{\\' + key + '}[0]{' + expr + '}\n'
        self.f.write('\\newcommand{\\')
        self.f.write(key)
        self.f.write('}[0]{')
        self.f.write(expr)
        self.f.write('}\n')
        self.content.append(key)
    

    def __enter__(self):
        self.f = open(self.path, 'w')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.f.close()
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_traceback}')

    def cheatsheet(self):
        name = Path(self.path.stem + '-cheatsheet.tex')
        with open(name, 'w') as f:
            f.write('\\documentclass[a4paper, 10pt]{article}\n')
            f.write('\\usepackage[margin=20mm]{geometry}\n')
            f.write('\\usepackage{bbold}\n')
            f.write('\\usepackage{amsmath}\n')
            f.write('\\usepackage{amssymb}\n')
            f.write('\\usepackage{amsthm}\n')
            f.write('\n')
            f.write('% Your commands come from that file\n')
            f.write('\\input{' + str(self.path) + '}\n')
            f.write('\n')
            f.write('\\begin{document}\n')
            f.write('\\hrule\n')
            f.write('\\vspace{3mm}\n')
            f.write('\\centerline{\\large Cheatsheet for {\\tt ' + self.path.stem + '.tex}}\n')
            f.write('\\vspace{3mm}\n')
            f.write('\\hrule\n')
            f.write('\\vspace{5mm}\n')
            f.write('\\begin{eqnarray*}\n')
            for k in self.content[:-1]:
                f.write('\\mbox{\\tt \\textbackslash ' + k + '} & : & \\')
                f.write(k)
                f.write(' \\\\\n')
            if len(self.content) > 0:
                kc= self.content[-1]
                f.write('\\mbox{\\tt \\textbackslash ' + k + '} & : & \\')
                f.write(k)
                f.write(' \n')
            f.write('\\end{eqnarray*}\n')
            f.write('\\end{document}\n')
    
