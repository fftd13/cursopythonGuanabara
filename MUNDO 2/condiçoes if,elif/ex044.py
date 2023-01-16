print('{:=^31}'.format(' CoffeShop dois irmãos '))
p = float(input('digite o valor da compra: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão cartao
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
o = int(input('digite a opção: '))
if o == 1:
    desconto = p - (p * 10 / 100)
    print('''você recebeu 10% de desconto por pagar à vista!
sua compra de R${:.2f} custara R${:.2f} '''.format(p,desconto))
elif o == 2:
    desconto = p - (p * 5 / 100)
    print('''você ganho 5% de desconto
sua compra R${:.2f} custara R${:.2f}'''.format(p,desconto))
elif o == 3:
    parcela = p / 2
    print('''você parcelou sua compra de R${:.2f} em 2x de R${:.2f}'''.format(p,parcela))
elif o == 4:
    nparcelas = int(input('digite a quantidade de parcelas que deseja fazer: '))
    juros = p + (p * 20 / 100)
    parcela = juros / nparcelas
    print('''você parcelou sua compra em {}x de R${:.2f}
sua compra de R${:.2f} custara R${:.2f} no final.'''.format(nparcelas,parcela,p,juros))
else:
    print('opção invalida')