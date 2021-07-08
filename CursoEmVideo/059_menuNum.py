num1 = float(input('Primeiro número: '))
num2 = float(input('Segund número: '))
command = 4
while command != 5:
    command = int(input('O que deseja fazer?\n'
                        '[1] somar\n'
                        '[2] multiplicar\n'
                        '[3] dividir\n'
                        '[4] entrar novos números\n'
                        '[5] sair\n'
                        '--> '))
    if command == 1:
        print(f'{num1} + {num2} = {num1+num2}')
    elif command == 2:
        print(f'{num1} x {num2} = {num1*num2}')
    elif command == 3:
        print(f'{num1} / {num2} = {num1/num2:.2f}')
    elif command == 4:
        num1 = float(input('Primeiro número: '))
        num2 = float(input('Segund número: '))
    elif command == 5:
        print('FIM')
    else:
        print('Valor incorreto')
    print(10*'=')
