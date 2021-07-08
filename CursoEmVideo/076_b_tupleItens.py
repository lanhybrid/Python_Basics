listagem = ('Caneta', 2, 'Lapis', 1.5, 'Caderno', 7.35, 'Estojo', 4.50, 'Post It pack', 2.99,
            'Sulfite 500', 24.80, 'Cartucho Print', 45, 'Abajur', 36.45, 'Notebook 5G', 3450.87)
print(42*'-')
print(f'{"LISTA DE COMPRAS":^42}')
print(42*'-')
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R$ {listagem[item]:>7.2f}')
   # print(f'{listagem[iteM]:.<30} R$ {listagem[priCe]:>8.2f}')
print(42*'-')