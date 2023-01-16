def leiaint(n=''):
    leia = input(f'{n}')
    while not leia.isnumeric():
        print('\033[0;31mERRO| ISSO NÃO É UM INT MALANDRO!!!\033[m')
        leia = input(f'{n}')
    leia = int(leia)
    return leia


a = leiaint(f'ler: ')
print(a)
