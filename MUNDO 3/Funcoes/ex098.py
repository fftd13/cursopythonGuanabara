from time import sleep


def contador(a, b, c):
    print(f'cotando de {a} a {b}')
    sleep(0.5)
    if c > 0:
        for cont in range(a, b + 1, c):
            print(f'{cont} ', end='')
            sleep(0.5)
    elif c < 0:
        for cont in range(a, b - 1, c):
            print(f'{cont} ', end='')
            sleep(0.5)
    print()


contador(1, 10, 1)
contador(10, 0, -2)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
dqnt = int(input('De quanto em quanto: '))
contador(inicio, fim, dqnt)
