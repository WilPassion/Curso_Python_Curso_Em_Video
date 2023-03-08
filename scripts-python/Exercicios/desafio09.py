print('====== TABUADA ====== \n')

tabuada = int(input('Você deseja a tabuada de qual número? '))
cont = 0

while(cont < 10):
    cont = cont + 1
    print('{} x {} = {}'.format(tabuada, cont, (tabuada * cont)))


