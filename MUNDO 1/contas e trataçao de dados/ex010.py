print('conversor de dollar\nseu dinheiro sera convertido em dollar!')
reais=float(input('insira a quantidade de dinheiro R$'))
d=reais//5.37
s=reais%5.35
print('voce pode comprar US${} dollares com R${}'.format(d,reais))
print('sobram R${:.2f}'.format(s))
