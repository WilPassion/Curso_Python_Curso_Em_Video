#desafio55 - Faça um programa que leia o peso de cinco pessoas. No final,
# mostre qual foi o maior
# e o menor pesos lidos
maior = 0
menor = 0
for i in range(1, 6):
  peso = float(input('Peso da {}º pessoa: '.format(i)))
  if i == 1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso
print('O maior peso é {}kg'.format(maior))
print('O menor peso é {}kg'.format(menor))