lista = []
while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
    lista
print(f'Você digitou {len(lista)} valores')
lista.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é {lista}')
if 5 in lista:
    print('O numero 5 esta na lista.')
else:
    print('O valor 5 não esta na lista.')