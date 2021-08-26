# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario
# introducirá las palabras en español e inglés separadas por dos puntos, y cada par
# `<palabra>:<traducción>` separados por comas. El programa debe crear un diccionario con las
# palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para
# traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

diccionario = {}
pregunta = 's'
# formacion del diccionario
while pregunta == 's':
     palabra = input('Ingrese la palabra con el siguente formato `<palabra>:<traducción>`: ')
     filtro = palabra.find(':')
     diccionario[palabra[0:filtro]] = palabra[filtro+1::]
     pregunta = input('Desea agregar otra palabra: s/n? : ')

print("Prueba del diccionario")
frase = input('ingrese una frase en espanol para ser traducida: ')
palabras = frase.split()

for x in palabras:
    print(diccionario.get(x , x) , end=' ')
