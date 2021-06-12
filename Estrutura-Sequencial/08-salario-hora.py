salariohora = input('Valor da hora trabalhada: ')
horames = int(input('Horas trabalhadas no mês: '))
mes = input('Mês de calculo: ')
salariomes = float(salariohora) * horames
print(f'No mês de {mes} foram trabalhadas {horames} horas \nSalário: {salariomes:.2f}')
