preço=float(input('preço do produto R$:'))
desconto=preço-(preço*5/100)
print('o preço do seu produto é R${},com 5% de desconto o preço é R${:.2f}'.format(preço,desconto))
