print('\033[1;31;40m -=-\033[m'*7)
print('\033[1;35;40m Analisando triangulos\033[m'+'\033[0;40m \033[m'*6)
print('\033[1;31;40m -=-\033[m'*7)
a = float(input('digite a primeira medida:'))
b = float(input('digite a segunda medida:'))
c = float(input('terceira medida:'))
if a + b > c and a + c > b and b + c > a:
    print('os tres segmentos formam um trinagulo')
else:
    print('os tres segmentos nao formam um triangulo')