from datetime import date

print('Grupo de maioridade!')
ano = date.today().year
maior = 0
menor = 0
for x in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?: '.format(x)))
    idade = ano - nasc
    if idade < 18:
        menor += 1
    else:
        maior += 1
if menor == 0:
    print('''Ao todo temos {} maiores de idade
e nenhum menor de idade'''.format(maior))
elif maior == 0:
    print('''Ao todo temos {}  menores de idade
e nenhum maior de idade'''.format(menor))
else:
    print('''Ao todo temos {} maior(es) de idade
e {} menor(es) de idade'''.format(maior,menor))