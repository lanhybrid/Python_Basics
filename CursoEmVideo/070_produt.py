total = milMore = c = valorBarato = 0
barato = ' '
while True:
    conti = False
    prod = input('Nome do produto: ')
    valor = float(input('Valor do produto R$ '))
    total += valor      #SOMA DOS PRODUTOS

    if c == 0 or valor < valorBarato:
        barato = prod
        valorBarato = valor   #DEFINIR PRODUTO MAIS BARATO
    c += 1

    if valor >= 500: milMore += 1   #DEFINIR PRODUTOS QUE CUSTAM MAIS DE 500
    cont = ' '

    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ').strip().upper()[0]
    print(10 * '=')
    if cont == 'N': break

print(f'Total da compra: R${total:.2f}\n'
      f'- {milMore} produtos custam mais de R$500\n'
      f'- {barato} foi o produto mais barato\n')
