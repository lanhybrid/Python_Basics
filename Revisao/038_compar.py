num = int(input('Digite o primeiro número: '))
num2 = int(input('Próximo: '))
if num > num2:
    print(f'{num} é o Maioral')
elif num < num2:
    print(f'{num2} é o Maioral')
else:
    print(f'São iguais...')
