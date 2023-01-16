def metade(valor, form=False):
    res = valor / 2
    return res if form is False else moeda(res)


def dobro(valor, form=False):
    res = valor * 2
    return res if form is False else moeda(res)


def aumentar(valor, taxa, form=False):
    res = valor + (valor * taxa / 100)
    return res if form is False else moeda(res)


def diminuir(valor, taxa, form=False):
    res = valor - (valor * taxa / 100)
    return res if form is False else moeda(res)


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')


def resumo(v, a, d):
    print(f'{"RESUMAÇO":^25}')
    print(f'metade do valor: {metade(v, form=True)}')
    print(f'dobro do valor: {dobro(v, form=True)}')
    print(f'aumento de {a}%: {aumentar(v, a, form=True)}')
    print(f'decrescimo de {d}%: {diminuir(v, d, form=True)}')