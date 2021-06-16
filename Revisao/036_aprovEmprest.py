print('--Bem vindo ao Banco emprestimo pra toda vida--')
emprestimo = float(input('Qual o valor do emprestimo? R$ '))
salario = float(input('Qual o seu salário mensal? R$ '))
tempo = int(input('Em quantos anos pretende pagar o emprestimo? '))
meses = tempo * 12
limite = salario * 0.3
prestacoes = emprestimo / meses

print(f'O emprestimo de R${emprestimo:.2f} será dividido em {tempo} anos ou {meses} meses\n'
      f'Valor das parcelas será de R${prestacoes:.2f} por mês')

if prestacoes >= limite:
    print('Emprestimo RECUSADO')
else:
    print('Emprestimo APROVADO')