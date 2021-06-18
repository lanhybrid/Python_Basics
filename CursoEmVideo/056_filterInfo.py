totalAge = 0
oldManAge = 0
oldMan = ''
contWom = 0

for c in range(1, 5):
    print(f'-= {c}ª Pessoa =-')
    name = input('Nome: ')
    age = int(input('Idade: '))
    sex = input('Sexo [M / F]: ').strip().upper()
    totalAge += age

    if sex == 'M':
        if age > oldManAge:
            oldManAge = age
            oldMan = name
    else:
        if age < 20:
            contWom += 1


mediAge = totalAge / 4
print(f'A média de idade é de: {mediAge} anos')
print(f'O homem mais velho é o {oldMan} com {oldManAge} anos')
print(f'E {contWom} mulheres são menores de 20 anos')
