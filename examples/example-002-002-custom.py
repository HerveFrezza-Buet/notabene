import notabene as nb

# There may be a lot of formulas that are not implemented yet in
# notabene. Among them, some are specific to you usage, and they do
# not need to belong to the notabene package, but rather to a bunch of
# assorted notations related to some of your specific work.

# This tutorial show you how to extend notabene.

#### Extend by python variables and functions

prototype, sample, t, rate = nb.to('\\omega \\xi \\tau \\alpha') # This parametrizes your notation.

def updating_rule(learnable, target, coef):
    return learnable@(t+1) == [1 - coef] * learnable@t + coef * target@t

#### Extend basic formulas

# let us define a new formula, that encloses some argument with a
# brace above and below (each one has a label). To do this, you can
# produce a basic formula. The Formula constructor needs a list of
# arguments (args) as well ad a function that produces the latex code
# as a string. Be sure to apply nb.to to all the arguments.

# This is the production of latex code.
def print_enclose(args):
    latex_code_what  = str(args[0]) 
    latex_code_below = '{' + str(args[1]) + '}' # Surrounding by braces is safer
    latex_code_above = '{' + str(args[2]) + '}' # Surrounding by braces is safer
    return '\\overbrace{\\underbrace{' + latex_code_what + '}_' + latex_code_below + '}^' + latex_code_above

# This is the formula
def enclose(what, below, above):
    return nb.basics.Formula([nb.to(what), nb.to(below), nb.to(above)],
                             print_enclose) # you may prefer a lambda here


#### We register some commands.

with nb.files.defs('002-002-custom.tex') as defs:
    nb.config.push('display style', True)
    defs.prefix = 'vq'
    
    defs['DefaultUpdate'] = updating_rule(prototype, sample, rate)
    defs['Update']        = updating_rule(nb.arg(2), nb.arg(3), nb.arg(1))

    defs['Enclose'] = enclose(updating_rule(prototype, sample, rate),
                              sample == sample@0,
                              nb.math.pi)

    defs['EncloseInTime'] = enclose(nb.arg(1), t-1, t+1)


    defs.cheatsheet() 


