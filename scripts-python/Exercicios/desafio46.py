#desafio46 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
# indo de 10 até 0
# com uma pausa de 1 segundo entre eles
from time import sleep
print('-=' * 25)
print('PREPARE-SE PARA O 13º FESTIVAL DE FOGOS!!!')
print('-=' * 25)
print('CONTAGEM REGRESSIVA...')
for i in range(10, -1, -1): # "primeiro - 1" para contar o 0
  sleep(1)
  print(i)
print('KABUM!!!')