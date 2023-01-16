# Faça um programa que tenha uma função chamada escreva(), que receba um
# texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(msg):
    tamanho = len(msg) + 6
    for c in range(0, tamanho):
        print('~', end='')
    print()
    print(f'   {msg}   ')
    for c in range(0, tamanho):
        print('~', end='')
    print()


for v in range(0, 3):
    mensagem = str(input('Digite algo: '))
    escreva(mensagem)
