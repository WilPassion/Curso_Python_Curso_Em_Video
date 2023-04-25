# Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas; o nome com todas as letras minúsculas; quantas letras ao todo (sem considerar os espaços); quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: '))

print('Analisando o seu nome...')

print('Seu nome em caracteres maiúsculos: {}'.format(nome.upper()))
print('Seu nome em caracteres minúsculos: {}'.format(nome.lower()))

contagem = nome.replace(' ', '')
print('Total de letras de seu nome: {}'.format(len(contagem)))

dividido = nome.split()

primeiro_nome = len(dividido[0])
print('Seu primeiro possui {} caracteres'.format(primeiro_nome))



