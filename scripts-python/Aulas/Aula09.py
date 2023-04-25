# Manipulação de string

print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s
It was popularised in the 1960s with the release of Letraset sheets containing 
Lorem Ipsum passages, and more recently with desktop publishing software like 
Aldus PageMaker including versions of Lorem Ipsum.""")

print('')

frase = 'Treinando com strings'

print(frase[6:21])
print(frase[6:])
print(frase[:6])
print(frase[6::2]) #posicao 6 ao fim de 2 em 2 caracteres
print(frase[6:19:3]) #posicao 6 a 19 de 3 em 3 caracteres

print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

print(frase.split())

frase2 = '   Curso em Vídeo Python - espaços antes e depois !  '

print('-'.join(frase2))

print(frase2)

print(frase2.split())

print(frase2.strip())
print(frase2.lstrip())
print(frase2.rstrip())

print('')

dividido = frase.split()

print(dividido)
print(dividido[3:3])

print('Vídeo' in frase2) #retorno boolean

print(frase2.replace('Vídeo','Faca'))

print(frase2.count('o')) #retorna quantos 'o's possui a cadeia de caracteres
print(len(frase2)) #retornar quantidade de caracteres contidos na var

print(frase2)
print(frase2.find('deo'))




