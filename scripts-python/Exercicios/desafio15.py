#desafio15 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dia pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.

km = float(input('Digite quantos km foram percorridos: '))
dias = int(input('Digite quantos dia o veículo foi locado: '))

total = (dias * 60) + (km * 0.15)

print('Total locação: {}'.format(total))