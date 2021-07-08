bras21 = 'Bragantino', 'Athletico-PR', 'Palmeiras', 'Fortaleza', 'Santos', 'Bahia', 'Atletico-GO', 'Atletico-MG', \
         'Fluminense', 'Flamengo', 'Corinthians', 'Ceara-SC', 'Internacional', 'Juventude', 'Sport Recife', \
         'America-MG', 'Cuiaba', 'Sao Paulo', 'Chapecoense', 'Gremio'
print('Os 5 primeiros:')
# 5 primeiros
for pos, nome in enumerate(bras21):
    if pos > 4:
        break
    print(f'{pos+1} - {nome}')
print('{:-^10}'.format('OU'))
print(f'{bras21[:5]}')
print(10*'-')
# 4 ultimos
print('Os últimos 4:')
for pos, nome in enumerate(bras21):
    if pos > 15:
        print(f'{pos+1} - {nome}')
print('{:-^10}'.format('OU'))
print(f'{bras21[-4:]}')
print(10*'-')
# Ordem alfabetica
print(sorted(bras21))
# Posição Chapecoense
print(10*'-')
print(f'Chapecoense está na posição: {(bras21.index("Chapecoense"))+1}')

