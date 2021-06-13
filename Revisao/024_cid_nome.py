cidade = input('Nome da cidade: ').strip().lower()
nome = input('Seu nome: ').strip()
print(f'A cidade inicia com Santo? {cidade[:6] == "santo "}')
print(f'Você é um Silva? {"silva" in nome.lower()}')
