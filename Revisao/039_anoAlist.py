from datetime import date
ano = int(input('Em qual ano você nasceu? '))
atual = date.today().year
idade = atual - ano
print(f'Este ano você completa {idade} anos')
if idade == 18:
    print('Você deve se alistar - ou não, esse ano')
elif idade > 18:
    print(f'Você deveria ter se alistado no ano de {ano + 18}')
else:
    print(f'Ainda faltam {18 - idade} anos para o seu alistamento\n'
          f'Volte em {ano + 18}')
