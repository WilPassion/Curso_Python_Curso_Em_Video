#desafio01 - Crie um script Python que leia o nome de uma pessoa e mostre a mensagem de boas-vindas de acordo com o valor digitado.

print('===== DESAFIO 01 =====')
nome = input('Qual é o seu nome? ')
print('É um prazer te conhecer,', nome, '!')

print('É um prazer te conhecer, {}!'.format(nome))
