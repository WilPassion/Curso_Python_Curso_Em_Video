#desafio09 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

print('====== TABUADA ====== \n')

tabuada = int(input('Você deseja a tabuada de qual número? '))
cont = 0

while(cont < 10):
    cont = cont + 1
    print('{}{} x {} = {}'.format('\033[1;31;40m', tabuada, cont, (tabuada * cont)))




