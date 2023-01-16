casa = float(input('digite o valor da casa:'))
salario = float(input('digite o valor do salario:'))
anos = int(input('em quantos anos voce pretende financiar?:'))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print('a prestaçao para pagar uma casa de {},'.format(casa),end = ' ')
print('em {} anos é de {:.2f}'.format(anos,prestaçao))
if prestaçao <= minimo:
    print('emprestimo concedido')
else:
    print('emprestimo negado')
