a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

if c < (a+b) and a < (b+c) and b < (a+c):
    print(f'{a}, {b} e {c} formam um triangulo.')
else:
    print(f'{a}, {b} e {c} NÃO formam um triangulo.')
