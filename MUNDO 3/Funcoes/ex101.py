
def voto(nasc):
    from datetime import date
    data_atual = date.today().year
    idade = data_atual - nasc
    if 65 > idade >= 18:
        return f'idade: {idade}\nPRECISA VOTA'
    elif idade < 16:
        return f'idade: {idade}\nNUM PRECISA VOTA'
    else:
        return f'idade: {idade}\nvoto opcional'


print(voto(2003))
print('-' * 20)
a = int(input('Digite o ano em que você nasceu: '))
print(voto(a))
