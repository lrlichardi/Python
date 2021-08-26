# Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su ID, y el
# valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo,
# preferente), donde “preferente” tendrá el valor True si se trata de un cliente preferente. El
# programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2)
# Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes,
# (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

BD = {1: {'nombre': 'lucas', 'direccion': 'per', 'telefono': '123', 'correo': '123', 'preferente': True},
2: {'nombre': 'lucas', 'direccion': 'per', 'telefono': '123', 'correo': '123', 'preferente': True}}
print('BASE DE DATOS EMPRESA FANTASMA')
opcion=''
while opcion != 6:
    print(' 1)Anadir cliente \n 2)Eliminar cliente \n 3)Mostrar cliente \n 4)Listar todos los clientes \n 5)Listar clientes preferentes \n 6)Terminar ')
    opcion = int(input('Que desea hacer? '))
    if(opcion == 1):
         print('Anadir cliente:')
         id = int(input('Ingrese id del cliente: '))
         BD[id] = {}
         nombre = input('Ingrese el nombre del cliente: ')
         BD[id]['nombre'] = nombre
         direccion = input('Ingrese la direccion del cliente: ')
         BD[id]['direccion'] = direccion
         telefono = input('Ingrese el telefono del cliente: ')
         BD[id]['telefono'] = telefono
         correo = input('Ingrese el Correo Electronico: ')
         BD[id]['correo'] = correo
         preferente = bool(input('Es cliente preferente?: '))
         BD[id]['preferente'] = preferente
         print('Cliente creado!')
         print(BD)
    elif (opcion == 2):
        print('Eliminar cliente')
        id = int(input('Ingrese id del cliente a borrar: '))
        eliminar = input(f'Seguro que desea eliminar al {BD[id]}')
        if(eliminar == 's' or eliminar == 'si' ):
            BD[id].clear()
    elif (opcion == 3):
        print('Mostrar cliente')
        id = int(input('Ingrese id del cliente a mostrar: '))
        print(BD[id])
    elif (opcion == 4):
        print('Mostrar todos los clientes')
        for x in BD:
            print(BD[x])
    elif(opcion == 5):
        print('Clientes preferentes') 
        for x in BD:
            if (BD[x]['preferente'] == True):
                print(BD[x])
        
        


