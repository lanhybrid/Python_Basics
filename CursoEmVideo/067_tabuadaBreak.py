while True:
    valor = int(input('Qual tabuada deseja ver? '))
    if valor < 0: break
    for c in range (0,11):
        print(f'{valor} x {c} = {valor*c}')
print('FIM')