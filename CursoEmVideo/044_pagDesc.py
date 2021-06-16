bruto = float(input('Valor da compra - R$ '))
formPag = int(input('Como deseja pagar?\n'
                    '[1] - Dinheiro a vista (10% desc)\n'
                    '[2] - Cartão (A vista / Credito)\n'
                    '->> '))
if formPag == 1:
    print(f'Pagamento a vista - 10% de desconto')
    print(f'Total: {bruto - bruto * 0.1}')
elif formPag == 2:
    card = int(input('Como deseja pagar?\n'
                     '[1] - A vista (5% de desconto)\n'
                     '[2] - Em 2 vezes\n'
                     '[3] - 3 à 12 vezes (20% Juros)\n'
                     '->> '))

    if card == 1:
        print(f'Pagamento a vista - 5% de desconto')
        print(f'Total: {bruto - bruto * 0.05}')
    elif card == 2:
        print(f'Pagamento em 2 vezes')
        print(f'Parcelas de R$ {bruto/2}')
    elif card == 3:
        parc = int(input('Quantas parcelas?\n'
                         '->> '))
        if parc > 12 or parc < 3:
            print('Valor incorreto')
        else:
            print(f'Pagamento em {parc} vezes')
        taxa = bruto + bruto * 0.20
        print(f'Valor com 20% Juros >> R${taxa:.2f}')
        print(f'{parc} parcelas de R$ {taxa/parc:.2f}')
    else:
        print('Valor incorreto - Tente novamente.')
else:
    print('Valor incorreto - Tente novamente.')
