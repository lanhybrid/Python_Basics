from random import randint
cont = 0
while True:
    print(10*'=')
    player1 = ' '
    while player1 not in 'IP':
        player1 = input('Par ou Impar? [P/I]: ').upper().strip()[0]
    num1 = int(input('Número de 0 a 5: '))
    num2 = randint(0, 5)
    soma = num1 + num2
    print(f'Player: {num1}, Computer: {num2}')
    print('Deu Par' if soma % 2 == 0 else 'Deu Impar')
    if player1 == 'P' and soma % 2 == 0 or player1 == 'I' and soma % 2 != 0:
        print('Você venceu')
    else:
        print('Você perdeu')
        break
    cont += 1
    player1 = ' '
print(10*'=')
print(f'Você venceu {cont} vezes')

