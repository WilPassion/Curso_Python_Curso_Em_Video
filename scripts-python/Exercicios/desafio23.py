# Faça um programa que leia um número de 0 a 9999 e mostra na tela cada um dos dígitos separados, exemplo: Digite um número: 1834
#Saída:
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 8

num = int(input('Digite um número entre 0 e 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(num))
print('Dezena: {}'.format(num))
print('Centena: {}'.format(num))
print('Milhar: {}'.format(num))
