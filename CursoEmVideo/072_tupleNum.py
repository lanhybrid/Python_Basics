numeros = "ZERO", "UM", "DOIS", "TRES", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVO", "DEZ", "ONZE", "DOZE", "TREZE", \
          "QUATORZE", "QUINZE", "DEZESSEIS", "DEZESSETE", "DEZOITE", "DEZENOVE", "VINTE "
while True:
    num = int(input('Entre um valor de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Valor incorreto, tente novamente')

print(f'O número {num} em extenso: {numeros[num]}')

