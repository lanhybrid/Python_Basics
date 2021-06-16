n1 = float(input('Nota de N1: '))
n2 = float(input(('Nota de N2: ')))
n3 = float(input(('Nota de N3: ')))
n4 = float(input(('Nota de N4: ')))
A1 = (n1+n2+n3+n4)/4
A2 = float(input('Nota de A2: '))
print(f'A1: {A1:.2f}\n'
      f'A2: {A2:.2f}')
print('LEMBRETE: A1 tem peso de 4.0, e A2 tem peso de 6.0 na média FINAL')
final = (A1*0.4)+(A2*0.6)
if final >= 6.0:
    print(f'Parabens, você foi aprovado com a média {final:.2f}')
elif final >= 4.5:
    print(f'Realize a prova de recuperação. Média {final:.2f}')
else:
    print(f'Reprovado, melhor sorte no próximo semestre. Média {final:.2f}')



