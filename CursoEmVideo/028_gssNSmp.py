from random import randint
from time import sleep
n = randint(1, 5)
print('Computador pensando em número de 1 a 5...')
sleep(2)
x = int(input('Adivinhe o número: '))
print('Você acertou!') if n == x else print(f'Errou!! O correto é {n}')
print('---FIM---')
