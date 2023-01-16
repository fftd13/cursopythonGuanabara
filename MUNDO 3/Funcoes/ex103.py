def ficha(n='deconhecido', g=0):
    return f'o jogador {n} fez {g} gols'


nome = str(input('Nome: ')).capitalize()
gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = int(0)
if nome.strip() == '':
    print(ficha(g=gols))
else:
    print(ficha(nome, gols))
