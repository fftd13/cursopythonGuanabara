from random import randint
import time
print('{:=^39}'.format(' PEDRA / PAPEL \ TESOURA '))
itens = ('pedra','papel','tesoura')
print(''' [ 0 ] - Pedra
 [ 1 ] - Papel
 [ 2 ] - Tesoura''')
opç = int(input('digite a sua opção: '))
comp = randint(0,2)
print('='*25)
print('o jogador jogou {}'.format(itens [opç]))
print('o computador jogou {}'.format(itens [comp]))
print('='*25)
if comp == 0:
    if opç == 0:
        print('empate')
    elif opç == 1:
        print('jogador ganhou!')
    elif opç == 2:
        print(' computador ganhou!')
    else:
        print('opção invalida')
elif comp == 1:
    if opç == 0:
        print('computador ganhou!')
    elif opç == 1:
        print('empate')
    elif opç == 2:
        print('jogador ganhou!')
    else:
        print('opção invalida')
elif comp == 2:
    if opç == 0:
        print('jogador ganhou!')
    elif opç == 1:
        print('computador ganhpu!')
    elif opç == 2:
        print('empate')
    else:
        print('opção invalida')
