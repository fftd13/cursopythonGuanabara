def notas(*n, sit=False):
    d = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n) / len(n)}
    if sit:
        if d['media'] >= 5:
            d['situacao'] = 'Boa'
        elif d['media'] < 5:
            d['situacao'] = 'Ruiml'

    return d


print(notas(10, 2, 3, 5, sit=True))
