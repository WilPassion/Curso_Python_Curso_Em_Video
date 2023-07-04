#desafio41 - A Confedereção Nacional de Natação precisa de um programa que leia o anos de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER
idade = int(input('Entre com a sua idade: '))
if idade >= 20:
  print('MASTER')
elif idade >= 19:
  print('SÊNIOR')
elif idade >= 14:
  print('INFANTIL')
else:
  print('MIRIM')