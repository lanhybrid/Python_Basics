num = int(input('Diga um número: '))
c = 0
for n in range(1, num+1):
    if num % n == 0:
        print('\33[33m', end=' ')
        c += 1
    else:
        print('\33[31m', end=' ')
    print(f'{n}', end=' ')
if c == 2:
    print(f'\n\033[mO número {num} é um número Primo')
else:
    print(f'\n\033[mO número {num} não é Primo')
