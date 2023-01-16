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
