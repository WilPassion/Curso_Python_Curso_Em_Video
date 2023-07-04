#desafio36 - Escreva um algoritmo que aprove o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Valor do imóvel: '))
salario = float(input('Valor do salário: '))
anos = int(input('Quantos anos de financiamento: '))
total_prestacao = valor_casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos '.format(valor_casa, anos), end='')
print('a prestação será de R${:.2f}'.format(total_prestacao))
if total_prestacao > salario * 0.30
  print('FINANCIAMENTO NEGADO')
else:
  print('FINANCIAMENTO APROVADO')