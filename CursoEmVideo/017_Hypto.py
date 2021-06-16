from math import hypot
cO = float(input('Cateto Oposto: '))
cA = float(input('Cateto Adjacente: '))
print(f'A soma do quadrado dos catetos <<{cO}, {cA}>> \né igual ao quadrado da Hipotenusa <<{hypot(cO,cA):.2f}>>')
