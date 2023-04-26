# Custo da Viagem - Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = float(input('Qual é a distância da viagem? Km: '))
if distancia <= 200:
    preco = distancia * 0.50
    print('O valor da viagem é R${:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('O valor da viagem é R${:.2f}'.format(preco))

# Resolução 2

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O valor da viagem é R${:.2f}'.format(preco))