import random
n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
Alunos = [n1, n2, n3, n4]
print(f'Aluno sorteado para apagar a lousa: {random.choice(Alunos)}')
random.shuffle(Alunos)
print(f'Ordem de apresentação dos trabalhos: {Alunos}')
