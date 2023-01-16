from random import randint

numeros = []


def sorteio():
    qtd_rand = randint(4, 10)
    for v in range(0, qtd_rand):
        rand_num = randint(0, 10)
        numeros.append(rand_num)


def somapar():
    soma = 0
    for s in range(0, len(numeros)):
        if numeros[s] % 2 == 0:
            soma += numeros[s]
    print(f'Somando os valores pares de {numeros} obtemos o valor {soma}')


sorteio()
somapar()
