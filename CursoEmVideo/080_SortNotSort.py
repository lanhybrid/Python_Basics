listThree = [0]
cont = 1
for c in range(5):
    nuM = int(input('Entre um número: '))
    #if cont == 1:
     #  listThree.append(nuM)
     #  print('Adicionado à lista')
    #else:
    for pos, item in enumerate(listThree):
        if nuM <= item:
            listThree.insert(pos, nuM)
            print(f'Adicionado na posição {pos}')
            break
        elif nuM > listThree[len(listThree)-1]:
            listThree.append(nuM)
            print('Adicionado no fim da lista')
            break
    #cont += 1
listThree.remove(0)
print(listThree)