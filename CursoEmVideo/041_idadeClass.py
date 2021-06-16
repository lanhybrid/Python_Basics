from datetime import date
nasc = int(input('Ano de nascimento (yyyy):  '))
idade = (date.today().year) - nasc
print(idade)
if idade <= 9:
    print(f'{idade} anos, Categoria MIRIM')
elif idade <= 14:
    print(f'{idade} anos, Categoria INFANTIL')
elif idade <= 19:
    print(f'{idade} anos, Categoria JUNIOR')
elif idade <= 25:
    print(f'{idade} anos, Categoria SÊNIOR')
else:
    print(f'{idade} anos, Categoria MASTER')
