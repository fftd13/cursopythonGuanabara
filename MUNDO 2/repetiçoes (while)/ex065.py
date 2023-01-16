opç = 'S'
cont = soma = maior = menor = 0
while opç in 'Ss':
    n = int(input('Digite um numero: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opç = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} numeros e a media foi {:.2f}'.format(cont,media))
print('O maior numero foi {} e o menor numero foi {}'.format(maior,menor))
