from random import randint
lista = []
jogos = []
quant = int(input('Quantos jogos devo palpitar?: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 100)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 50:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i} {l}')