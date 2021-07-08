listagem = ('Caneta', 2, 'Lapis', 1.5, 'Caderno', 7.35, 'Estojo', 4.50, 'Post It pack', 2.99,
            'Sulfite 500', 24.80, 'Cartucho Print', 45, 'Abajur', 36.45, 'Notebook 5G', 3450.87)
print(42*'-')
print(f'{"LISTA DE COMPRAS":^42}')
print(42*'-')
iteM = 0
priCe = 1
leng = int(len(listagem)/2)
for c in range(leng):
    print(f'{listagem[iteM]:.<30} R$ {listagem[priCe]:>8.2f}')
    iteM += 2
    priCe += 2
print(42*'-')