soma = count = 0
while True:
    x = int(input('Digite um número para somar: '))
    if x == 999: break
    soma += x
    count += 1
print(f'A soma dos {count} números é de {soma}')
