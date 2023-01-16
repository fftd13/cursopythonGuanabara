import moeda

v = float(input('Digite um valor: '))
print(f'A metade de R${v} é R${moeda.metade(v)}')
print(f'O dobro de R${v} é R${moeda.dobro(v)}')
print(f'O valor R${v} aumentado em 10% é R${moeda.aumentar(v, 10)}')
print(f'O valor R${v} diminuido em 10% é R${moeda.diminuir(v, 10)}')
