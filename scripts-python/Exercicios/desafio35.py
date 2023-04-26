# Analisando Triângulo - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('ANÁLISE DE TRIÂNGULOS \n')
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas FORMAM UM TRIÂNGULO')
else:
    print('As retas NÃO FORMAM UM TRIÂNGULO')