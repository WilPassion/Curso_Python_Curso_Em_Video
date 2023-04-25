# Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra "A"; em que posição ela aparece a primeira vez; em que posição ela aparece pela última vez.

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra a apareceu {} vezes'.format(frase.count('A')))

print('A primeira letra "a" apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra "a" apareceu na posição {}'.format(frase.rfind('A')+1))