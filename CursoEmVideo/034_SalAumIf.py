salario = float(input('Valor do salario: '))
if salario >= 1250:
    print(f'Você terá 10% de aumento >>> R$ {salario+salario*0.10:.2f}')
else:
    print(f'Você terá 15% de aumento >>> R$ {salario + salario * 0.15:.2f}')
