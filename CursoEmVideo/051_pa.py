n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
nx = 0
for n in range(1, 11):
    print(f'n{n} ->>', n1 + razao*nx)
    nx += 1

an = n1 + (10 - 1) * razao
print('n10 =', an)
