name = input('Nome completo: ').strip()

print(f'1 - UPPER: {name.upper()}')
print(f'2 - lower: {name.lower()}')

lenght = len(name) - name.count(' ')
print(f'3 - Nome com {lenght} letras')

lista = name.split()
print(f'4 - O nome {lista[0]} possuí {len(lista[0])} letras')
