p = float(input('digite o peso: '))
a = float(input('digite a altura: '))
imc = p/(a**2)
print('seu imc é {:.1f}'.format(imc),end='')
if imc < 18.5:
    print(',você esta abaixo do peso ')
elif 25 <= imc < 30:
    print(',você esta com sobrepeso')
elif 30 <= imc < 40:
    print(',você esta obeso')
elif imc > 40:
    print(',você esta em estado de obesidade morbida')
else:
    print(',você esta no peso ideal')
