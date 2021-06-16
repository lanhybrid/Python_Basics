speedy = int(input('Velocidade do carro em Km/h: '))
print('Limite de velocidade: 80Km/h')
if speedy > 80:
    print(f'Você está acima do limite estabelecido. Multado em R${(speedy-80)*7:.2f}')
else:
    print('Boa viagem')
