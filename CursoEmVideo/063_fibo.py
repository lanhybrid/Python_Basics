n = int(input('Quantos números da sequencia de Finonacci deseja ver? '))
f1 = 0
f2 = 1
c = 0
while c < n-1:
    if c == 0:
        print(f'{f1} -> {f2} ', end='')
    else:
        f3 = f1 + f2
        print(f'-> {f3} ', end='')
        f1 = f2
        f2 = f3
    c += 1
