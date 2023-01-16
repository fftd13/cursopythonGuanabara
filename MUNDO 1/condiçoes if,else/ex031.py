distancia = float (input ('distancia:'))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('o valor sera:{}'.format(valor))
#valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45