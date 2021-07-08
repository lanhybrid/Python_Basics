num = 0
sum = 0
cont = 0
flag = 'S'
maior = 0
menor = 0

while flag in 'Ss':
    num = int(input('Digite um número para somar: '))
    if cont == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    sum += num
    cont += 1
    flag = input('Continuar? [S/N]')
print(f'Você entrou entrou {cont} números, com soma de {sum}\n'
      f'O maior númereo foi {maior} e o menor foi {menor}\n'
      f'A média foi {sum/cont:.2f}')

