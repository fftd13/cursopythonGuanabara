numero1 = int (input ('1º numero:'))
numero2 = int (input ('2º numero:'))
numero3 = int (input ('3º numero:'))
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
maior = numero2
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
if numero3 > numero2 and numero3 > numero1:
    maior = numero3
print ('o maior numero é {}'.format(maior))
print ('o menor numero é {}'.format(menor))
