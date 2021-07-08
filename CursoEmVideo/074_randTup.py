from random import randint
sort = randint(0, 100), randint(0, 100), randint(0,100),\
       randint(0, 100), randint(0, 100)
maior = menor = count = 0

print(f'Valores sorteados: ', end='')
for n in sort:
    print(n, end=' ')
#    if count == 0:
 #       maior = menor = n
  #  else:
   #     if n > maior:
    #        maior = n
     #   if n < menor:
      #      menor = n
   # count += 1

print(f'\nMaior valor sorteado: {max(sort)}')
print(f'Menor valor sorteado: {min(sort)}')


