import math
num = float(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz quadrada de {} é {}'.format(num, math.ceil(raiz)))
print('A raiz quadrada é {}'.format(math.floor(raiz)))
print('A raiz quadrada é {:.2f}'.format(raiz))