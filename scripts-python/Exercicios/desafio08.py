#desafio08 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Digite o valor para conversão(m): '))

centimetro = metro * 100
milimetro = metro * 1000

print('{}m = {}cm'.format(metro, centimetro))
print('{}m = {}mm'.format(metro, milimetro))