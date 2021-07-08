print('---USING WHILE---')
fact = int(input('Qual número deseja ver o fatorial? '))
result = 1
print(f'{fact}! = ', end='')
while fact >= 1:
    print(f'{fact} ', end='')
    print('x 'if fact > 1 else '= ', end='')
    result *= fact
    fact -= 1
print(result, '\n')

print('---USING FOR---')
fact2 = int(input('Qual número deseja ver o fatorial? '))
result2 = 1
print(f'{fact2}! = ', end='')
for c in range(fact2, 0, -1):
    if c > 1:
        print(f'{c} x ', end='')
    else:
        print(f'{c} = ', end ='')
    result2 = result2 * c
print(result2, '\n')