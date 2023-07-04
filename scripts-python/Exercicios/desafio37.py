#desafio37 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:
# 1 para binario
# 1 para octal
# 3 para hexadecimal
from time import sleep
print('-=-' * 20)
print('{:>40}'.format('CONVERSOR BASES NUMÉRICAS'))
print('-=-' * 20)
decimal = int(input('Entre com o valor inteiro a ser convertido: '))
opcao = int(input('Escolha a base para conversão: \n [1] Binário \n [2] Octal \n [3] Hexadecimal \n'))
sleep(2)
if opcao == 1:
   binario = bin(decimal)[2:]
   print('O número {} em binário é: {}'.format(decimal, binario))
elif opcao == 2:
  octal = oct(decimal)[2:]
  print('O número {} em octal é: {}'.format(decimal, octal))
elif opcao == 3:
  hexadec = hex(decimal)[2:]
  print('O número {} em hexadecimal {}'.format(decimal, hexadec))
else:
  print('Opção inválida. Tente')
