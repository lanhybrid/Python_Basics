
while True:
    valor = int(input('Qual valor deseja sacar? R$'))
    if valor % 10 == 0: break
    print('Valor incorreto, deve ser multiplo de 10')
total = valor
cont = 0
ced = 200
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if cont > 0:
            print(f'Total de {cont} cedulas de R${ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        cont = 0
        if total == 0: break






