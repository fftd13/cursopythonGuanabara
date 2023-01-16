def fatorial(a, b=False):
    c = 1
    for f in range(a, 0, -1):
        if b:
            print(f, end='')
            if f > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        c *= f
    return c


print(fatorial(5, True))
