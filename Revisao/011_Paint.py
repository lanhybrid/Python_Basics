from math import ceil
alt = float(input('Qual a altura da parede? '))
lar = float(input('E a largura? '))
area = alt * lar
tinta = area / 2
print(f'Para uma area de {area:.2f}m2 será necessário {ceil(tinta)}L de tinta')