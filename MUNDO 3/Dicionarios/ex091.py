from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador 1': randint(1,6),
             'jogador 2': randint(1,6),
             'jogador 3': randint(1,6),
             'jogador 4': randint(1,6)}
ranking = []
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(1)
print('.')
sleep(0.5)
print('-=-'*10)
print(f'{"- = RANKING = -":^30}')
print('-=-'*10)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
