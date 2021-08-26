# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo
# guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene
# <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

datos = {}
nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
direccion = input('Ingrese su direccion: ')
tel = input('Ingrese su tel: ')

datos['Nombre'] = nombre
datos['Edad'] = edad
datos['direccion'] = direccion
datos['tel'] = tel

print(datos)