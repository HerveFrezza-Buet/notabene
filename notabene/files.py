from . import basics

class defs:
    def __init__(self, path):
        self.path = path;
        self.prefix = None

    
    def __setitem__(self, at, value):
        if self.prefix:
            key = '{}{}'.format(self.prefix, at)
        else:
            key = at
        self.f.write('\\newcommand{\\')
        self.f.write(key)
        self.f.write('}[0]{')
        self.f.write(str(basics.to(value)))
        self.f.write('}\n')
    

    def __enter__(self):
        self.f = open(self.path, 'w')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.f.close()
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_traceback}')
