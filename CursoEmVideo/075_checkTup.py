a = int(input('Digite um número: '))
b = int(input('Digite outro num: '))
c = int(input('Digite um número: '))
d = int(input('Again... '))
e = int(input('Vai o ultimo: '))
ordem = (a, b, c, d, e)
print(ordem)
print(f'O número 9 apareceu: {ordem.count(9)} vezes') if 9 in ordem else print('O dia esta lindo')
print(f'O número 3 esta na posição: {ordem.index(3)+1}') if 3 in ordem else print('dont know any three')
#Pares
cont = 0
print('Os números pares foram: ', end='')
for n in ordem:
    if n % 2 == 0:
        print(n, end=' ')
        cont += 1
if cont == 0: print('não teve números pares, você deveria saber,'
                    'foi você que os digitou.')

