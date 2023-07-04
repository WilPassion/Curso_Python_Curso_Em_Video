#desafio42 - Refaça o desafio 35 dos triângulos acrescentado o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lador diferentes
print('ANÁLISE DE TRIÂNGULOS \n')
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas PODEM FORMAR um triângulo ->', end='')
    if reta1 != reta2 != reta3 != reta1:
        print(' EQUILÁTERO')
    elif reta1 != reta2 != reta3 != reta1:
        print(' ESCALENO')
    else:
        print(' ISÓSCELES')
else:
    print('As retas NÃO FORMAM um triângulo')