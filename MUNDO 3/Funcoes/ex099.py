from time import sleep


def maior(*num):
    maior_num = 0
    print('Valores: ', end='')
    for m in range(0, len(num)):
        if num[m] > maior_num:
            maior_num = num[m]
        print(f'{num[m]} ', end='')
    print()
    print(f'Quantidade de valores: {len(num)}')
    print(f'Maior valor: {maior_num}')
    print('-' * 30)


maior(1, 5, 6, 7)
sleep(3)
maior(6, 2, 8, 3, 15, 12)
