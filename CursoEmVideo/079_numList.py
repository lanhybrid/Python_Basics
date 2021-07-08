listTwo = list()
while True:
    num = int(input('Entre um número '))
    if num not in listTwo:
        listTwo.append(num)
        print('Valor adicionado')
    else:
        print('Valor duplicado, não adicionado')
    while True:
        cue = input('Deseja continuar? [S/N]  ').strip()[0]
        if cue in 'SsNn':
            break
        print('Opção incorreta')
    if cue in 'Nn':
        break
listTwo.sort()
print(listTwo)
