import notabene as nb

# With notabene, you can also define latex commands with
# arguments. The nb.arg(i) formula is the placeholder for argument i.

i, n = nb.to('i n')
serie = nb.sets.byext(nb.arg(1)@0, ..., nb.arg(1)@i, ..., nb.arg(1)@n)@(nb.sets.isin(i, nb.arg(2)))


with nb.files.defs('commands.tex') as defs:
    defs.prefix = 'ex'
    
    defs['Serie'] = serie

    defs['Polar'] = nb.arg(1) * nb.math.e**(nb.math.i * nb.arg(2))

    defs.cheatsheet() 



