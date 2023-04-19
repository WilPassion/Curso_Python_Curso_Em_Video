#desafio04 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possível sobre ela.

a = input('Type something: ')

print('The primitive type is', type(a))
print('Are there upper letters? ', a.isupper())
print('Are there lower letters? ', a.islower())
print('Is capitalized? ', a.istitle())
print('Is alpha numeric? ', a.isalpha())

    