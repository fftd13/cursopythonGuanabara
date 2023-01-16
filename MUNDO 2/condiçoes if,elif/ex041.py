from datetime import date

nasc = int(input('digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('o atleta tem: {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')
