#desafio43 - Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule o IMC e mostre o seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
print('-=-' * 20)
print('{:>35}'.format('CALCULADORA IMC'))
print('-=-' * 20)
peso = float(input('Digite o seu peso em kg: '))
alt = float(input('Digite a sua altura: '))
imc = peso / (alt * alt)
if imc > 40:
  print('Obesidade Mórbida')
elif imc > 30:
  print('Obesidade')
elif imc > 25:
  print('Sobrepeso')
elif imc > 18.5:
  print('Peso ideal')
else:
  print('Abaixo do Peso')