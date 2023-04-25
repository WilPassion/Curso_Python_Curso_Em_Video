# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO".

cidade = str(input('Digite o nome da cidade: ')).strip().upper()

dividido = cidade.split()

print('O nome da cidade é: {}'.format(cidade))

print(cidade[:5] == 'SANTO')
print('SANTO' in dividido[0])

