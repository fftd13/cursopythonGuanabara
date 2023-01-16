from time import sleep
opç = 0
pv = int(input('Digite o primeiro valor: '))
sv = int(input('Digite o segundo valor: '))
while opç != 5:
    print('''[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - NOVOS NUMEROS
[5] - SAIR''')
    opç = int(input('Digite sua opção: '))
    if opç == 5:
        print('Programa finalizado.')
    elif opç == 1:
        print('{} + {} = {}'.format(pv,sv,pv + sv))
    elif opç == 2:
        print('{} X {} = {}'.format(pv,sv,pv * sv))
    elif opç == 3:
        if pv > sv:
            maior = pv
        else:
            maior = sv
        print('Entre {} e {} o maior é {}'.format(pv,sv,maior))
    elif opç == 4:
        pv = int(input('Digite o primeiro valor: '))
        sv = int(input('Digite o segundo valor: '))
    else:
        print('Opção invalida,tente novamente')
    print('-=-'*8)
    print('Carregandinho ',end='')
    sleep(1)
    print('. ',end='')
    sleep(0.5)
    print('. ',end='')
    sleep(0.5)
    print('.')
