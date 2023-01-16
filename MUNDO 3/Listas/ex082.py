listag = []
par = []
impar = []
while True:
    v = int(input('DIgite um valor: '))
    listag.append(v)
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
    r = ' '
    while r not in 'SN':
        r = str(input('Continuar ? [S/N] : ')).strip().upper()[0]
    if 'N' in r:
        break
print(f'Você digitou {listag}')
print(f'esses sao os numeros pares da lista {par}')
print(f'esses sao os numeros impares {impar}')