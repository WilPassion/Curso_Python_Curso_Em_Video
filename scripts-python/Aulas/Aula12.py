## Aula 12 - Estrutura Condicional Aninhada

nome = str(input('Qual é o seu nome?'))
if nome == 'William':
  print('Seu nome tem origem inglesa, Will')
elif nome == 'Pedro' or 'Marcos' or 'Helen':
  print('Seu nome é popular no Brasil')
elif nome in 'Cida Carlinhos Maycon':
  print('Nome interessante!')
else:
  print('Treinando Condicional em Python')