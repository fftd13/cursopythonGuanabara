print('Este numero é primo ?')
numero = int(input('digite o numero: '))
total =  0
for x in range(1,numero + 1):
    if numero % x == 0:
        print('\033[0m',end='')
        total += 1
        #total = total + 1
    else:
        print('\033[31m',end='')
    print(x,end=' ')
print('\no número {} foi dividido {} vezes'.format(numero,total))
if total == 2:
    print('portanto {} é um numero primo'.format(numero))
else:
    print('portanto {} não é um numero primo'.format(numero))
