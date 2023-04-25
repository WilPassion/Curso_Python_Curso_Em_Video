# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

cidade = str(input('Digite o nome da cidade: ')).strip()

print('Seu nome tem Silva? {}'.format('SILVA' in cidade.upper()))
