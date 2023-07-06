#desafio56 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo -->          media_idade
# Qual é o nome do homem mais velho -->          var maior_idade
# Quantas mulheres têm menos de 20 anos -->             menor_20
soma_idade = 0
maior_idade_homem = 0
total_mulher20 = 0
for i in range(1, 5):
  print('----- {}º PESSOA -----'.format(i))
  nome = str(input('Nome: '))
  idade = int(input('Idade: '))
  sexo = str(input('Sexo[F/M]: ')).upper().strip()
  soma_idade += idade

  #resolvendo "nome do homem mais velho" no primeiro laço -> "i == 1"
  if i == 1 and sexo in 'H':
    maior_idade_homem = idade
    nomevelho = nome
  # resolvendo maior idade de "maior_idade_homem"
  if sexo in 'M' and idade > maior_idade_homem:
     maior_idade_homem = idade
     nomevelho = nome

  #resolvendo "Quantas mulheres têm menos de 20 anos"
  if sexo in 'F' and idade < 20:
    total_mulher20 += 1

print('A média de idade do grupo é {}'.format(soma_idade/4))
print('O homem mais velho tem {} e tem {} anos'.format(maior_idade_homem, nome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(total_mulher20))