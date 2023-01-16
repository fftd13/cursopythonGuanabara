num = int(input('digite o numero:'))
print('''escolha a base da conversão:
[ 1 ] BINARIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opçao = int(input('digite a opção:'))
if opçao == 1:
    print('{} em binario é igual a  {}'.format(num,bin(num)[2:]))
elif opçao == 2:
    print('{} em octal é igual a {}'.format(num,oct(num)[2:]))
elif opçao == 3:
    print('{} em hexadecimal é igual a {}'.format(num,hex(num)[2:]))
else:
    print('opçao invalida tente novamente')
