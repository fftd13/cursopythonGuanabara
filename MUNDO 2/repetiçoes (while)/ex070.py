soma = mmil = cont = vpmp = 0
pmb = ''
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço R$:'))
    soma += valor
    cont += 1
    if valor >= 1000:
        mmil += 1
    if cont == 1 or valor < vpmb:
        pmb = nome
        vpmb = valor
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar ? [S/N]:')).strip().upper()[0]
    print('-'*24)
    if r == 'N':
        break
print(f'o valor total da compra foi R${soma:.2f}')
print(f'temos {mmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {pmb} que custa {vpmb:.2f}')

