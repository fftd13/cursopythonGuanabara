print('aluguel:R$60.00/dia\nKm rodados:R$0.15/Km')
d=int(input('digite o numero de dias:'))
km=float(input('digite o numero de Km:'))
al=d*60
kmr=km*0.15
total=al+kmr
print('voce alugou o carro por {} dias,portanto pagara:{:.2f}'.format(d,al))
print('você rodou {}Km portanto pagara:R${:.2f}'.format(km,kmr))
print('totalizando em:R${:.2f}'.format(total))
