import random

# Solicita os nomes dos alunos
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

# Adiciona os nomes em uma lista e embaralha a ordem
lista = [n1, n2, n3, n4]
random.shuffle(lista)

# Exibe a ordem de apresentação
print('A ordem de apresentação será:')
print(lista)
