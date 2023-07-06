#desafio49 - Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço FOR
print('-=' * 20)
print('{:>22}'.format('TABUADA'))
print('-=' * 20)
num = int(input('Digite um número para cálculo da tabuada: '))
for i in range(0, 11):
  print('{} x {} = {}'.format(num, i, num*i))