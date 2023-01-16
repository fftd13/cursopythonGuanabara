num = 'zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
while True:
    while True:
        extenço = int(input('Digite um numero de 0 a 20: '))
        if 0 <= extenço <= 20:
            break
        print('tente novamente')
    print('Voce digitou o numero {}'.format(num[extenço]))
    resp = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('fim')
