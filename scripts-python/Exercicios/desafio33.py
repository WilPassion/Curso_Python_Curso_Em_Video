# Maior e menor valores - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
# Verificabndo o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num2 > num3:
    num3 = maior
# Verificabndo o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))

