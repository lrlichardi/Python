# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre
# una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le
# pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del
# diccionario.

persona = {}
key = ''
while not key == 'salir':
    key = input('Ingrese el tipo de dato NOMBRE EDAD DIRECCION ,ETC : ')
    if key != 'salir':
        value = input('Ingrese el dato: ')
        persona[key] = value
        print(persona)  
   
    


