pn = float(input('digite a primeira nota:'))
sn = float(input('digite a segunda nota:'))
media = (pn + sn)/2
print('a media do aluno foi: {}'.format(media))
if media < 5:
    print('o aluno foi reprovado')
elif media >= 7:
    print('o aluno foi aprovado')
else:
    print('o aluno esta de recuperaçâo')