#desafio47 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
for i in range(2, 52, 2):
  if i % 2 == 0:
    print(i, end='. ') # --> print -> 2. 4. 6. 8. 10. 12. 14. 16. 18
print('FIM')