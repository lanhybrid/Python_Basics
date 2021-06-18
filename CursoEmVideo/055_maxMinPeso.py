maxPeso = 0
minPeso = 0
for c in range(0, 5):
    peso = int(input('Entre um peso: '))
    if c == 0:
        maxPeso = peso
        minPeso = peso
    else:
        if peso > maxPeso:
            maxPeso = peso
        if peso < minPeso:
            minPeso = peso

print(f'Maior peso: {maxPeso}Kg')
print(f'Menor peso: {minPeso}Kg')
