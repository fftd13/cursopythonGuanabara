def ajuda(com):
    help(com)


while True:
    comando = str(input('Comando: '))
    if comando.upper() == 'FIM':
        break
    else:
        print(ajuda(comando))
