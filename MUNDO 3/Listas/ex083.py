expr = str(input('Digite a expressão: ')).strip()
pilha = []
for carac in expr:
    if carac == '(':
        pilha.append('(')
    elif carac == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('valido')
else:
    print('invalido')
