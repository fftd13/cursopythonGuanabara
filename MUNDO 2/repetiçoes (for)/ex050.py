print('Digite 6 numeros\nO pytgon ira somar apenas os numeros pares')
s = 0
for x in range(1,7):
    n = int(input('digite o {}º numero:'.format(x)))
    if n % 2 ==0:
        s += n
print(s)