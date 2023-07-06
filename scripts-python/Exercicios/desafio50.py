#desafio50 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o
s = 0
count = 0
for i in range(0, 6): # Usar VAR i para controle ao invés do num
  num = int(input('Digite um número: '))
  if num % 2 == 0:
    s += num
    count += 1
print('O resultado da soma dos {} digitados é {}'.format(count, s))