n1 = int(input('Primeiro n: '))
n2 = int(input('Segundo n: '))
n3 = int(input('Terceiro n: '))
menor = n1
maior = n3
#Checando menor:
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Checando maior:
if n1 > n3 and n1 > n2:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')