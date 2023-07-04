#desafio44 - Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
# à vista em dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% juros
preco = float(input('Digite o valor do produto: R$'))
forma_pagto = int(input('Forma de pagamento: \n [1] Dinheiro/Cheque à vista \n [2] Cartão à vista \n [3] Cartão parcelamento 2x \n [4] Cartão parcelamento 3x \n'))
if forma_pagto == 1:
  preco_final = preco - (preco * 0.1)
  print('Valor total: R${:.2f}'.format(preco_final))
elif forma_pagto == 2:
  preco_final = preco - (preco * 0.05)
  print('Valor total: R${:.2f}'.format(preco_final))
elif forma_pagto == 3:
  preco_final = preco / 2
  print('Sua compra será parcela em 2x de R${:.2f}'.format(preco_final))
elif forma_pagto == 4:
  qtdade_parcelas = int(input('Quantas parcelas: '))
  preco_final = preco + (preco * 0.2)
  valor_parcela = preco_final / qtdade_parcelas
  print('Sua compta será parcelada em {} vezes de R${:.2f} - '.format(qtdade_parcelas, valor_parcela), end='')
  print('Valor final: R${:.2f}'.format(preco_final))
else:
  print('Opção inválida')