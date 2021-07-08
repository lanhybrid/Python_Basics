n1 = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
nx = 0
z = 10
while nx < z:
    print(n1 + razao * nx, end=' -> ')
    nx += 1
    if nx == z:
        q = int(input('\nDeseja ver mais quantos termos? '))
        z += q