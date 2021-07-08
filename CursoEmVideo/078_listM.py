oneList = list()
for c in range(5):
    oneList.append(int(input('Digite um número: ')))
oneMin = min(oneList)
oneMax = max(oneList)

print(f'O maior número foi {oneMax} na posição ', end='')
for pos, num in enumerate(oneList):
    if num == oneMax:
         print(f'{pos}...', end='')

print(f'\nO menor número foi {oneMin} na posição ', end='')
for pos, num in enumerate(oneList):
    if num == oneMin:
        print(f'{pos}...', end='')