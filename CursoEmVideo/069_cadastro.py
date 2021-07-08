age = men = w20 = 0

while True:
    sexo = ' '
    cont = ' '

    print(10 * '=')
    idade = int(input('Idade: '))
    while sexo not in 'FM':
        sexo = input('Sexo [F/M]: ').upper().strip()[0]
    if idade >= 18: age += 1
    if sexo == 'M': men += 1
    if sexo == 'F' and idade < 20: w20 += 1

    while cont not in 'SN':
        cont = input('Continuar? [S/N] ').upper().strip()[0]
    if cont == 'N': break

print(10 * '=')
print(f'{age} maiores de 18 anos\n'
      f'{men} homens foram cadastrados\n'   
      f'{w20} mulheres tem menos de 20 anos\n')
