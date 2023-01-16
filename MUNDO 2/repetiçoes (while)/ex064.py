n = cont = soma = 0
n = int(input('Digite um numero [999 pra para]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero [999 pra para]'))
print('Você digitou {} numeros, a soma deles foi {}'.format(cont,soma))