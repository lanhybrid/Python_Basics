sex = str(input('Entre seu sexo [M/F]: ')).strip()[0]
while sex not in 'MmFf':
    print('Valor incorreto')
    sex = str(input('Entre seu sexo [M/F]: '))
print(f'Sexo == {sex.upper()}')
