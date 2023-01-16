# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
def area(a, b):
    ter = a * b
    print(f'a area de um terreno {a} X {b} é de {ter}m²')


altura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(altura, comprimento)
