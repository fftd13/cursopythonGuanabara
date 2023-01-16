from random import randint
val = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
maior = menor = ''
print('os valores sorteados foram: ',end='')
for n in val:
    print(f'{n} ',end='')
print(f'\nO maior foi {max(val)}')
print(f'O menor valor foi {min(val)}')