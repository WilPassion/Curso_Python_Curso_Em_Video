#desafio54 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade
# e quanto já são maiores
from datetime import datetime
ano_atual = datetime.now().year
idade = 0
maiores = 0
menores = 0
for i in range(1, 8):
  ano = int(input('Em que anos a {}º pessoa nasceu? '.format(i)))
  idade = ano_atual - ano
  if idade >= 18:
    maiores += 1
  else:
    menores += 1
print('Total de maiores de idade: {}'.format(maiores))
print('Total de menores de idade: {}'.format(menores))