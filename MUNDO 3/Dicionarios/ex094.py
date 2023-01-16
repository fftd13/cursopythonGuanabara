pessoas = []
acima_media = []

pessoa = {}

soma_idade = 0
idade = 0

continuar = True
while continuar:
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('[M/F] Sexo: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO DE DIGITAÇÃO !!!')
    while True:
        idade = input('Idade: ')
        if idade.isnumeric():
            pessoa['idade'] = int(idade)
            break
        print('ERRO DE DIGITAÇÃO !!!')
    soma_idade += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        continue_ask = str(input('[S/N] Continuar ?: ')).upper()
        if continue_ask in 'SN':
            break
        print('ERRO DE DIGITAÇÃO')
    if continue_ask == 'N':
        break

media = int(soma_idade / len(pessoas))

print(f'Foram cadastradas um total de {len(pessoas)} pessoas')
print(f'A média de idade entre as pessoas da lista é de {media}')
print(f'lista de mulheres cadastradas:')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f' - {p["nome"]}')
print(f'Pessoas com a idade maior que a média({media} anos):')
for p in pessoas:
    if p['idade'] > media:
        print(f' - {p["nome"]} com {p["idade"]} anos')
