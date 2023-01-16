ficha_jogador = {}
golPpartida = []

ficha_jogador['NOME'] = str(input('Nome do jogador: '))
tot_ptd = int(input('Quantas partidas jogadas?: '))

for p in range(0, tot_ptd):
    qts_gols = int(input(f' Quantos gols na {p + 1}º partida: '))
    golPpartida.append(qts_gols)

ficha_jogador['GOLS'] = golPpartida[:]
ficha_jogador['TOTAL'] = sum(golPpartida)

print('-' * 40)
print(ficha_jogador)
print('-' * 40)

for k, v in ficha_jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-' * 40)
print(f'O jogador {ficha_jogador["NOME"]} jogou {tot_ptd}')

for i, v in enumerate(golPpartida):
    print(f'Partida {i + 1}: {v} Gols')
print(f'Foram {ficha_jogador["TOTAL"]} gols no total')
