# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente, exemplo: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Digite o seu nome completo: ')).strip()

print('Analisando seu nome...')

print('O seu nome completo é {}'.format(nome))

dividido = nome.split()

print('Primeiro nome: {}'.format(dividido[0]))
print('Último nome: {}'.format(dividido[len(dividido)-1]))

