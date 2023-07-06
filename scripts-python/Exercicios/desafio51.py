#desafio51 - Desenvolva um programa que leia o primeiro termo e a a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão
# formula an = a1 + (n - 1) * r
print('-=' * 25)
print('{:>35}'.format('PRIMEIROS 10 TERMOS DA PA'))
print('-=' * 25)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
n = a1 + (10 - 1) * r #formula
for i in range(a1, n + r, r): # Necessário calcular o decimo/nsimo termo -> for i in range(a1, "10", r) - ACIMA
  print('{}'.format(i), end=' -> ')
print('FIM')