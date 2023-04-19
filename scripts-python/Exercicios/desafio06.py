#desafio06 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math
n = int(input('Digite um número: '))

print('Dobro: {}'.format(n * 2))
print('Triplo: {}'.format(n * 3))
print('Raiz Quadrada: {:.0f}'.format(math.sqrt(n)))

