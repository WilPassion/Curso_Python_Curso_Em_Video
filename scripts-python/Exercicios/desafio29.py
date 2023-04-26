# Radar eletrônico - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

print('-=-' * 20 )
print('RADAR ELETRÔNICO')
print('-=-' * 20 )
vel = float(input('Qual é a velocidade em que o veículo está percorrendo? '))
if vel > 80:
    print('MULTADO! Você ultrapassou o limite de velocidade que é 80km/h ')
    multa = (vel - 80) * 7
    print('Você deverá arcar com uma multa no valor de R${:.2f}'.format(multa))
print('Tenha um bom dia! Siga em segurança!')