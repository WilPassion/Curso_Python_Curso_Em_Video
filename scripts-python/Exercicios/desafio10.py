#desafio10 - Crie um progama que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,23.

money = float(input('Type the amount of money that you have R$: '))

print('You can get US${:.2f}'.format(money / 3.23))