numero = int(input('digite um numero para calcular seu fatorial:'))
c = numero
f = 1
while c > 0:
    f *= c
    print('{}'.format(c),end='')
    print(' X ' if c > 1 else ' = ',end='')
    c -= 1
print(f)
