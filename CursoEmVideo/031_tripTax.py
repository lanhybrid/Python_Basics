dist = int(input('Qual a distancia da viagem: '))
print(f'Distancia: {dist}Km')
if dist <= 200:
    tkt = dist*0.5
else:
    tkt = dist*0.45
print(f'Valor da passagem - R${tkt:.2f}')
