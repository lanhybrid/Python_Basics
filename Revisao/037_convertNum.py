num = int(input('Digite um número inteiro: '))
print('Qual base de conversção deseja realizar?\n'
      '[1] para binario\n[2] para octal\n[3] para hexadecimal')
choice = int(input())
if choice == 1:
    print(f'{num:b}')
elif choice == 2:
    print(f'{num:o}')
elif choice == 3:
    print(f'{num:x}')
else:
    print('Valor não aceito')

