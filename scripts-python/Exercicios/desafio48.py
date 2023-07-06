#desafio48 - Faça um programa que calcule a soma entre todos os número ímpares
# que são múltiplos de três
# e que se encontram no intervalo de 1 até 500
soma = 0
count = 0
for i in range(1, 501, 2):
  if i % 3 == 0:
    count += 1
    soma = soma + i
print('A soma de todos os {} valores solicitados é {}'.format(count, soma))