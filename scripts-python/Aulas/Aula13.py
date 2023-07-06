# Aula13

# for c in range(0, 5) --> inicia no zero, pois contagem não considera última volta do laço

for c in range(0, 5):  # resultado - 5x
  print('Hello World')
print('The End')

for c in range(0, 6):
  print(c)
print('The End')

for c in range(7, 0, -1):   #-1 -> representa a iteração - contador regressivo
  print(c)
print('The End')

for c in range(0, 11, 2): #contar de 0 a 10, pulando 2
  print(c)
print('The End')

num = int(input('Digite um número: '))
for c in range(0, num+1):
  print(c) #-> variável controle
print('The End')

i = int(input('Início contagem: '))
f = int(input('Fim da contagem: '))
p = int(input('Passo(pular): '))
for c in range(i, f+1, p):
  print(c)
print('The End')

s = 0
for c in range(0, 3):
  n = int(input('Digite um valor para a soma: '))
  s += n # s = s + n
print('O resultado da soma é {}'.format(s))

#TESTE DATA ATUAL
from datetime import datetime
ano_atual = datetime.now().year
print(ano_atual)