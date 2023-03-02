nome = str(input('Digite seu nome: '))

#NOME VAI OCUPAR 20 ESPACOS
print('Olá, {:20}!' .format(nome))

#ALINHAMENTO

print('Olé, {:>30}!' .format(nome))
print('Olá, {:<30}!' .format(nome))
print('Olá, {:^30}!' .format(nome))
