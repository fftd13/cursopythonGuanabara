from datetime import date

nasc = int(input('digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade == 18:
    print('você tem que se alistar IMEDIATAMENTE')
elif idade > 18:
    qf = idade - 18
    print('voce ja deveria ter se alistado ha {}'.format(qf))
    ano = atual - qf
    print('em {}'.format(ano))
else:
    qf = 18 - atual
    print('faltam {} anos para seu alistamento'.format(qf))
    ano = atual + qf
    print('seu alistamento sera em {} anos'.format(ano))