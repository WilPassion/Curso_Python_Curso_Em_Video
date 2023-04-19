#desafio11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

lar = float(input('Digite a largura: '))
alt = float(input('Digite o tamanho: '))

area = lar * alt

print('Você vai precisar de {} litros'.format(area / 2))
