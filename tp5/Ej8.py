# Escribir un programa que pida al usuario una palabra/frase e informe por pantalla si es un
# palíndromo.

palabra = input('Ingrese una frase!: ')

array_palabra = list(palabra)
reverso_palabra = array_palabra.copy()
reverso_palabra.reverse()
if array_palabra == reverso_palabra:
    print('Es un palindromo')
else:
    print('No lo es')    


