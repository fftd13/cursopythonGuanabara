pessoas = []
dados = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Deseja continuar ?[S/N]: ')).strip().upper()[0]
    if sn in 'N':
        break
print(f'Ao todo foram {len(pessoas)} pessoas cadastradas.')
print(f'o maior peso foi {mai}Kg, de ',end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]',end='')
print()
print(f'O menor peso foi de {men}Kg, de ',end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]',end='')
print()