n1 = int(input('digite o 1º numero: '))
n2 = int(input('digite o 2º numero: '))
if n1 > n2:
    print('''o maior valor é {}
o menor valor é {}'''.format(n1,n2))
elif n1 < n2:
    print('''o maior valor é {}
o menor valor é {}'''.format(n2,n1))
else:
    print('os dois valores são iguais')