while True:
    cont = 0
    num = int(input('Digite o numero da tabuada que você quer ver: '))
    if num < 0:
        break
    while cont <= 10:
        print(f'{num} X {cont} = {num * cont}')
        cont += 1
print('FIM')