import moeda

v = float(input('Digite um valor: '))
print(f'A metade de {moeda.moeda(v)} é {moeda.metade(v, form=True)}')
print(f'O dobro de {moeda.moeda(v)} é {moeda.dobro(v, form=True)}')
print(f'O valor {moeda.moeda(v)} aumentado em 10% é {moeda.aumentar(v, 10, form=True)}')
print(f'O valor {moeda.moeda(v)} diminuido em 10% é {moeda.diminuir(v, 10, form=True)}')
