# Jogo da Adivinhação - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

print('===== JOGO DA ADIVINHAÇÃO =====')
from random import randint
from time import sleep
computador = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar... ')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
if computador == jogador:
    print('PARABÉNS!!! Você conseguiu me vencer =D')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))



