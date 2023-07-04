#desafio39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alista ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou o prazo
age = int(input('Type your age: '))
if age > 18:
  register = age - 18
  print('\nThe time for your registration on the Selective Service System has passed {} year(s), you would better be hurry!'.format(register))
elif age < 18:
  register = 18 - age
  print('\n You have {} year(s) until your registration on the Selective Service System, be ready'.format(register))
else:
  print('\n It is time to register yourself on the Selective Service System, young man!')