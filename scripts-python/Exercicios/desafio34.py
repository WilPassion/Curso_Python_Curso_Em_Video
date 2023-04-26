# Aumentos múltiplos - Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários supiores a R$1.200,00, calcule um aumento de 10%. Para inferiores ou iguais o aumento é de 15%.

from time import sleep
print('-=-' * 20)
print('REAJUSTE SALARIAL')
print('-=-' * 20)
sal = float(input('Digite o valor do seu salário: R$'))
print('-=-' * 20)
print('Calculando... \n')
sleep(2)
if sal <= 1200:
    reajuste = sal * 0.15
    sal_total = reajuste + sal
else:
    reajuste = sal * 0.10
    sal_total = reajuste + sal
print('O valor do aumento será R${:.2f}. Valor salário bruto atualizado: R${:.2f}'.format(reajuste, sal_total))
