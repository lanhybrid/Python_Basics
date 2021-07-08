lista = ('cachorro', 'gato', 'hipopotamo', 'leao', 'gazela', 'rinoceironte', 'arara',
         'urso', 'papagaio', 'mico leao dourado', 'tucano')
vogals = ('a', 'e', 'i', 'o', 'u')
for animal in lista:
    print(f'\nNa palavra {animal.upper()} temos ', end='')
    for letra in animal:
        if letra in vogals:
            print(letra, end=' ')