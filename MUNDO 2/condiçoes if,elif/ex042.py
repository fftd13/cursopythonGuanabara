print('digite o valor dos lados do triângulo')
a = float(input('primeiro segmento: '))
b = float(input('segundo segmento: '))
c = float(input('terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('os segmentos formam um triangulo', end='')
    if a == b == c:
        print(' EQUILATERO')
    elif a != b != c != a:
        print(' ESCALENO')
    else:
        print(' ISOSCELES')
else:
    print('os segmentos nao formam um triangulo!')
