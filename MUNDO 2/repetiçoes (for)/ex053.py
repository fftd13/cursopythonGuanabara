print('Esta frase é um palíndromo?')
frase = str(input('\nDigite uma frase qualquer: ')).strip().upper()
separada = frase.split()
junto = ''.join(separada)
#inverso = junto[::-1]
inverso = ''
for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]
print('A frase {} ao contrario é {}'.format(junto,inverso))
if junto == inverso:
    print('esta frase é um palíndromo')
else:
    print('esta frase não é um palíndromo')
