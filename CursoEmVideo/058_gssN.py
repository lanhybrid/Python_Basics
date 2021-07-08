from random import randint
compN = randint(0, 10)
guest = int(input('Adivinhe o número de 0 a 10\n'
                  '--> '))
cont = 1
acertou = False
while not acertou:
    guest = int(input('Errou... tente outra vez\n'
                      '--> '))
    if compN == guest:
        acertou = True
    cont += 1
if cont == 1:
    print('FANTASTICO, acertou de primeira')
else:
    print(f'Acertou em {cont} tentativas')
