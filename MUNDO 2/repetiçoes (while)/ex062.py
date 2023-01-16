print('Gerador de PAs')
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = pt
contador = 1
#contador2 = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{} →'.format(termo),end=' ')
        contador += 1
        #contador2 +=1
        termo += r
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais?: '))
    print('progressão finalizada com {} termos mostrados'.format(total))
print('FIM')
        #if contador == 10:
            #print('PAUSE')
            #mt = int(input('Quantos termos você quer mostrar mais?: '))
            #if mt == 0:
                #print('progressão finalizada com {} termos mostrados'.format(contador2))
            #else:
                #contador -= mt
