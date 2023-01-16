ficha = []

while True:
    nome = str(input('NOME:'))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar?[s/n]: ')).upper()
    if resp in 'N':
        break
print('-=-' * 23)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('_' * 25)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar qual ficha de qual aluno?[999 para encerrar]: '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}')

