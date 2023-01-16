from random import shuffle

x = input ('digite o nome do aluno:')
x2 = input ('digite o nome do aluno:')
x3 = input ('digite o nome do aluno:')
x4 = input ('digite o nome do aluno:')
x5 = input ('digite o nome do aluno:')
lista=[x,x2,x3,x4,x5]
shuffle(lista)
print('a ordem de alunos é:\n {}'.format(lista))

