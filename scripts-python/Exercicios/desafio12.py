#desafio12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prod = float(input('Digite o preço do produto R$: '))
desc = prod - (prod * 5 / 100)

print('O preço do produto apos o desconto e desconto R${:.2f}'.format(desc))
