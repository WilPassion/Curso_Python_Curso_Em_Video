number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))

s = number1 + number2
m = number1 * number2
d = number1 / number2
di = number1 // number2
p = number1 ** number2
dr = number1 % number2

print('Soma: {}, Multiplicação: {}, Divisão: {:.2f}, Divisão Inteira: {}'.format(s, m, d, di), end=' >>> ')
print('Potência: {}, Resto Divisão: {}'.format(p, dr))