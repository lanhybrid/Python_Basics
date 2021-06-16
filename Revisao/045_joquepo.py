from time import sleep
from random import randint
p1 = int(input('Vamos jogar:\n[0] Pedra\n[1] Papel\n[2] Tesoura\n'
      'Escolha seu sinal >>> '))
if p1 in (0, 1, 2):         #VALIDA A JOGADA
    itens = ('PEDRA', 'PAPEL', 'TESOURA')
    comp = randint(0, 2)
    sleep(.5)
    print('Joo..', end='')
    sleep(.5)
    print('Quei..', end='')
    sleep(.5)
    print('Powww!')
    sleep(.5)
    print(f'\nPlayer 1 ==> {itens[p1]}\n'
          f'Computer ==> {itens[comp]}\n')
    if p1 == comp:
        print(f'Empate! Ambos jogaram {itens[comp]}')
    elif p1 == 0:       #PLAYER JOGA PEDRA
        if comp == 1:
            print(f'Computer WINS!')
        else:
            print(f'Player 1 WINS')
    elif p1 == 1:       #PLAYER JOGA PAPEL
        if comp == 2:
            print(f'Computer WINS!')
        else:
            print(f'Player 1 WINS')
    elif p1 == 2:       #PLAYER JOGA TESOURA
        if comp == 0:
            print(f'Computer WINS!')
        else:
            print(f'Player 1 WINS')
else:
        sleep(.5)
        print('Something went wrong... try again...')



