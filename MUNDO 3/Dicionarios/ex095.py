def erro_d():
    print('ERRO DE DIGITAÇÃO !!!')


ficha_jogador = {}

lista_jogadores = []
gols = []

totgols = 0

while True:
    ficha_jogador["nome"] = str(input('Nome do jogador: '))
    while True:
        aux = input(f'Quantas partidas {ficha_jogador["nome"]} jogou?: ')
        if aux.isnumeric():
            partidas_jogadas = int(aux)
            break
        erro_d()

    for p in range(0, partidas_jogadas):
        golpPartida = int(input(f'Quantos gols na partida {p+1}: '))
        totgols += golpPartida
        gols.append(golpPartida)

    ficha_jogador['gols'] = gols[:]
    ficha_jogador['total'] = totgols

    lista_jogadores.append(ficha_jogador.copy())
    ficha_jogador.clear()
    gols.clear()
    totgols = 0

    print('-=-' * 30)
    while True:
        continuar = str(input('Quer continuar?[S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        erro_d()
    if continuar in 'N':
        break
print('-*-' * 30)
for i in lista_jogadores:
    print(f'{i}')
dado_jog = int(input('Mostrar dado de qual jogador?: '))
for i, g in enumerate(lista_jogadores[dado_jog]["gols"]):
    print(f'partida {i+1}|gols: {g}')
