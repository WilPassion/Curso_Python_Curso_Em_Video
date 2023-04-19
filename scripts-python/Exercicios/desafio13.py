#desafio13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de desconto.

sal = float(input('Digite o seu salário: R$'))

desc = sal - (sal * 5 / 100)

print('Seu salário com desconto é R${:.2f}'.format(desc))
