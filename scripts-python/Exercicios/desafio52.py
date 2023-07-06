#desafio52 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = 0
total = 0
num = int(input('Digite um número: '))
for c in range(1, num +1):
  if num % c == 0:
    print('\033[33m', end='')
    total += 1
  else:
    print('\033[31m', end='')
  print('{}'.format(c), end=' ')
print('\n\033[0mO número {} foi divisível {} vezes'.format(num, total))
if total == 2: # Se "total" de vezes que o número digitado for divisível por "c" for = a 2 (regra primo)
  print('O NÚMERO É PRIMO')
else:
  print('O NÚMERO NÃO É PRIMO')