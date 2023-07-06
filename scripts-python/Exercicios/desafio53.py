#desafio53 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #separar - vetor/lista
junto = ''.join(palavras) #juntar
#inverso = junto[::-1] -> solução 2
inverso = ''
for letra in range(len(junto) -1, -1, -1 ): #(len conta qtdade de caracteres, primeiro -1 vai até posição -1, -1 looping/letters decrease)
  inverso += junto[letra]
if junto == inverso:
  print('Temos um palíndromo')
else:
  print('Não temos um palíndromo')