from random import randint
cont = 0
while True:
    ndj = int(input('Escolha um numero:'))
    jog = str(input('Par ou Impar?[P/I]: '))
    comp = randint(1,10)
    poi = (ndj + comp) % 2
    if jog in 'Pp':
        if poi == 0:
            cont +=1
            print(f'Computador jogou {comp} e Você {ndj},a soma deu {comp + ndj} (Par)')
            print('Você ganhou!')
        if poi == 1:
            print(f'Computador jogou {comp} e Você {ndj},a soma deu {comp + ndj} (Impar)')
            print('O computador ganhou!')
            break
    if jog in 'Ii':
        if poi == 1:
            cont +=1
            print(f'Computador jogou {comp} e Você {ndj},a soma deu {comp + ndj} (Impar)')
            print('Você ganhou!')
        if poi == 0:
            print(f'Computador jogou {comp} e Você {ndj},a soma deu {comp + ndj} (Par)')
            print('O computador ganhou!')
            break
print(f'Você ganhou {cont} veze(s)')