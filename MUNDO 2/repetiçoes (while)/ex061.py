print('='*27)
print('{:^20}'.format('    10 TERMOS DE UMA PA'))
print('='*27)
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = pt
contador = 0
print('primeiro termo ',end='')
while contador <= 10:
    print('{} → '.format(termo),end='')
    termo += r
    contador += 1
print('FIM')
