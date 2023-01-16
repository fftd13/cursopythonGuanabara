m18 = hc = mm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-'*25)
    if idade >= 18:
        m18 += 1
    if sexo in 'M':
        hc += 1
    if idade < 20 and sexo == 'F':
        mm20 += 1
    ctn = ' '
    while ctn not in 'SN':
        ctn = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if ctn in 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {m18}.')
print(f'Ao todo temos {hc} homens cadastrados.')
print(f'E temos {mm20} mulheres com menos de 20 anos.')