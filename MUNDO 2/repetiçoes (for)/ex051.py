print('='*27)
print('{:^20}'.format('    10 TERMOS DE UMA PA'))
print('='*27)
pt = int(input('digite o primeiro termo:'))
r = int(input('digite a razao:'))
d = pt + 10 * r
for x in range(pt,d-1,r):
    print('{}'.format(pt + x), end = ' → ')
print('FIM')