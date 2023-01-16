'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.'''
print('CADASTRAR')

nome = str(input('Nome: '))
ano_n = int(input('Ano de nascimento: '))
idade = 2022 - ano_n
carteira_t = int(input('Carteira de trabalho: '))

if carteira_t > 0:
    ano_c = int(input('Ano de contratação: '))
    aposen = (ano_c - ano_n) + 35
    salario = float(input('Salário: '))

    cad = {'nome': nome,
           'idade': idade,
           'carteira de trabalho': carteira_t,
           'ano de contratação': ano_c,
           'salario': salario,
           'aposentadoria': aposen}
elif carteira_t == 0:
    cad = {'nome': nome,
           'idade': idade
           }
else:
    print('Carteira de trabalho nao identificada')
    cad = {'nome': nome,
           'idade': idade
           }
print('-=-'*10)
print(f'{"CADASTRO":^30}')
for k, v in cad.items():
    print(f'{k}: {v}')
