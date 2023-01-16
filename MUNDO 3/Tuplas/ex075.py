num = (int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')))
print(f'O numero 9 aparece {num.count(9)} vezes.')
if 3 in num:
    print(f'O numero 3 apareceu na posição {num.index(3)+1}.')
else:
    print('Não há nenhum número 3.')
print('Os números pares são ',end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ',end='')
