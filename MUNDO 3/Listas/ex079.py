lista = list()
while True:
   n = int(input('Digite um valor: '))
   if n not in lista:
       lista.append(n)
       print('valor adicionado com sucésso !')
   else:
       print('Valor já adicionado !')
   r = ' '
   while r not in 'SN':
       r = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
   if r in 'N':
      break
print(f'Você digitou os valores: {lista}')