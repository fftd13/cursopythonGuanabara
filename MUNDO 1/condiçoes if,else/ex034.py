sal = float(input('digite o salario R$:'))
if sal > 1250:
    aumento >= sal + (sal * 10 / 100)
    print('você recebeu um aumento de 10%')
else:
    aumento = sal + (sal * 15 / 100)
    print('você recebeu um aumento de 15%')
print('agora o seu salario é de:R${}'.format(aumento))
