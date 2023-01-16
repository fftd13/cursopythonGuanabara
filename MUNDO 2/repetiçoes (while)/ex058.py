from random import randint
print('----- JOGO DA ADVINHAÇÃO -----')
print('O computador escolhera um numero de 0 á 10\nTente advinhar!!!')
comp = randint(1,10)
td = 0
acertou = False
while not acertou:
    jogador = int(input('Qual o numero que o computador escolheu?: '))
    if jogador == comp:
        acertou = True
        print('O numero escolhido foi [{}]'.format(comp))
        print('você acertou')
    else:
        td += 1
        if jogador < comp:
            print('Mais...')
        elif jogador > comp:
            print('Menos...')
        print('Tente novamente')
print('Total de erros: [{}]'.format(td))
'''if jogador == comp:
    print('Você acertou!!!\nO computador escolheu o numero {}'.format(comp))
else:
    td += 1
    if jogador < comp:
        print('Mais...')
    if jogador > comp:
        print('Menos...')
    print('Tente novamente!')
while jogador != comp:
    jogador = int(input('Qual o numero que o computador escolheu?: '))
    if jogador == comp:
        print('Você acertou!!!\nO computador escolheu o numero {}'.format(comp))
    else:
        td += 1
        if jogador < comp:
            print('Mais...')
        if jogador > comp:
            print('Menos...')
        print('tente novamente!')
print('Total de erros: [{}]'.format(td))'''
