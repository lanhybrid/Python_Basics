import random
num = random.randint(0, 9999)
print(num)
#MATEMATICO
ml = num // 1000 % 10
ct = num // 100 % 10
dz = num // 10 % 10
un = num // 1 % 10
print("===Forma Matematica===")
print(f'Unidades: {un}')
print(f'Dezenas: {dz}')
print(f'Centenas: {ct}')
print(f'Milhar: {ml}')
#MANIPULAÇÃO > ainda esta falho
print("\n===Forma de Maniplação===")
nstr = str(num)
mun = nstr[::-1]
print(f'Unidades: {mun[0]}')
print(f'Dezenas: {mun[1]}')
print(f'Centenas: {mun[2]}')
print(f'Milhar: {mun[3]}')


