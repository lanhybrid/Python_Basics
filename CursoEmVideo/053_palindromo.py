original = input('Entre uma frase: ').strip()
oriSplit = original.lower().split()
oriJoin = ''.join(oriSplit)
size = len(oriJoin)
pali = ''
for letra in range(size, 0, -1):
    pali = pali + (oriJoin[letra-1])
if pali == oriJoin:
    print(f'A frase "{original}" é uma Palindromo')
else:
    print(f'A frase "{original}" não é uma Palindromo')



