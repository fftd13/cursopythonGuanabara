n = cont = s =  0
while True:
    n = int(input('digite um numero: '))
    cont += 1
    if n == 999:
        break
    s += n
print(f'a soma entre os {cont} numeros é igual a {s}')