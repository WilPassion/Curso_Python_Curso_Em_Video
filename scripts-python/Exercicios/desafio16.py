#desafio16 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. "Ex: Digite um número: 6.124". O número 6.124 tem a parte inteira 6.

import math
num = float(input('Digite um número real: '))

print('O número digitado é {} e sua porção inteira é {}'.format(num, math.floor(num)))
print('O número digitado é {} e sua porção fracionada é {}'.format(num, math.trunc(num)))
print('O número digitado é {} e sua porção fracionada é {}'.format(num, int(num)))

