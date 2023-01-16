dados_aluno = {}

dados_aluno['Nome'] = str(input('Nome: '))
media = float(input('Média: '))
dados_aluno['Média'] = media

print('--', '#'*15, '--')
for k, v in dados_aluno.items():
    print(f'{k} do aluno: {v}')
if media < 5.5:
    print('Reprovado')
else:
    print('Aprovado')