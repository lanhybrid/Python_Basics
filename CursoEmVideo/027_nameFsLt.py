nome = input('Qual seu nome jovem? ').strip()
lnome = nome.split()
print(f'O seu primeiro nome é {lnome[0]}')
print(f'O último nome é: {lnome[len(lnome)-1]}')
