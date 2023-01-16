palavras = (str(input('Digite uma palavra: ')).strip().upper(),
            str(input('Digite outra palavra: ')).strip().upper(),
            str(input('Digite outra palavra: ')).strip().upper(),
            str(input('Digite outra palavra: ')).strip().upper())
for v in palavras:
        print(f'\nna palavra {v} temos ',end='')
        for letra in v:
            if letra in 'AEIOU':
                print(letra,end=' ')