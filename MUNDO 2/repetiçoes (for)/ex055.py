print('Maior e menor peso!')
maior = 0
menor = 0
for x in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(x)))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('o maior peso é {}\ne o menor peso é {}'.format(maior,menor))

'''            gambiarra   
            
   maior = 0
   menor = 9999
   for x in range(1,4):
        peso = float(input('peso:'))
        if peso > menor:
            maior = peso
        else:
            menor = peso
   print(maior,menor)'''