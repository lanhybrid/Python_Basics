from datetime import date
ano = int(input('Ano para analisar - aperte 0 para ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'{ano} Bissexto')
else:
    print(f'{ano} não é bissexto')
