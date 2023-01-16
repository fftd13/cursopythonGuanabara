hmv = 0
nhmv = ''
soma = 0
mulheresm = 0
for x in range(1,6 - 1):
    print('----- {}º P E S S O A ------'.format(x))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    soma += idade
    sexo = str(input('Sexo [H/M]: ')).strip()
    if x == 1 and sexo in ('Hh'):
       hmv += idade
       nhmv += nome
    if sexo in ('Hh') and idade > hmv:
       hmv += idade
       nhmv += nome
    if sexo in ('Mm') and idade < 20:
        mulheresm += 1
media = soma // x
print('''A idade media do grupo é {} anos
O homem mais velho do grupo é {} com {} anos de idade'''.format(media,nhmv,hmv))
print('Existem {} mulhere(s) menores de 20 anos'.format(mulheresm))