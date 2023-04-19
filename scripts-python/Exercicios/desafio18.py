#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo: '))

rad = radians(ang)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print('O angulo digitado é {}'.format(ang))
print('Seno = {:.2f}'.format(seno))
print('Cosseno = {:.2f}'.format(cosseno))
print('Tangente = {:.2f}'.format(tangente))