a = 3
b = 5
c = 2
d = 4
x = 'X'
o = 'O'
sym = x


def make_line(sym):
    i = 0
    line = ''
    while i < b:
        line = line + (sym * 3)
        if sym == x:
            sym = o
        else:
            sym = x
        i += 1
    print(line)


iii = 0
while iii < d:
    ii = 0
    while ii < c:
        make_line(sym)
        ii += 1
    if sym == x:
        sym = o
    else:
        sym = x
    iii += 1


