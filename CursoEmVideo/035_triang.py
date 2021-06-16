a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

if c < (a+b) and a < (b+c) and b < (a+c):
    if a == b == c:
        tipo = 'Equilatero'
    elif a == b or a == c or b == c:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
    print(f'{a}, {b} e {c} formam um triangulo {tipo}.')
else:
    print(f'{a}, {b} e {c} NÃO formam um triangulo.')


