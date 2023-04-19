#desafio17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

hip = (co ** 2 + ca ** 2) ** (1/2)
hip2 = hypot(co, ca)

print('A hipotenusa é {}'.format(hip))
print('A hipotenusa é {}'.format(hip2))


