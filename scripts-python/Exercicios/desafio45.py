#desafio45 - Crie um programa que faça o computador jogar Jokempô com você
from random import randint
from time import sleep
print('-=' * 15)
print('{:>25}'.format('JOKEMPÔ'))
print('-=' * 15)
opcao_jogada = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('Suas opções: \n [0] PEDRA \n [1] PAPEL \n [2] TESOURA')
player = int(input('Qual é a sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 15)
print('O jogador jogou {}'.format(opcao_jogada[player]))
print('O computador jogou {}'.format(opcao_jogada[computador]))
print('-=' * 15)
if computador == 0: # PEDRA
  if player == 0:
    print('EMPATE')
  elif player == 1:
    print('JOGADOR VENCE')
  elif player == 2:
    print('COMPUTADOR VENCE')
  else:
    print('JOGADA INVÁLIDA!')
elif computador == 1: # PAPEL
  if player == 0:
    print('COMPUTADOR VENCE')
  elif player == 1:
    print('EMPATE')
  elif player == 2:
    print('JOGADOR VENCE')
  else:
    print('JOGADA INVÁLIDA!')
elif computador == 2: # TESOURA
  if player == 0:
    print('JOGADOR VENCE')
  elif player == 1:
    print('COMPUTADOR VENCE')
  elif player == 2:
    print('EMPATE')
  else:
    print('JOGADA INVÁLIDA!')