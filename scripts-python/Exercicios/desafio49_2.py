#desafio49.2 - Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço FOR - Adicionado CORES
print('-=' * 20)
print('{:>22}'.format('TABUADA'))
print('-=' * 20)
num = int(input('Digite um número para cálculo da tabuada: '))
for i in range(0, 11):
  if i % 2 == 0:
    print('{}{} x {} = {}{}'.format('\033[36m', num, i, num*i, '\033[0m'))
  else:
    print('{} x {} = {}'.format(num, i, num*i))