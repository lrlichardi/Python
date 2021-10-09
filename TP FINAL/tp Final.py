# 1) Agregar un nuevo auto al inventario
# 2) Eliminar un auto del inventario por ID.
# 3) Mostrar un auto del inventario por ID.
# 4) Mostrar el listado de todos los IDs y la marca/modelo del auto que corresponde a ese ID, ordenado
# por ID en orden creciente.
# 5) Mostrar el listado de todos los IDs y el modelo y precio ordenado en orden creciente.
# 6) Informar cuantos autos hay cargados en el inventario.
# 7) Marcar un auto como reservado por ID.
# 8) Mostrar el listado de todos los IDs y modelos que hayan sido marcados como reservados.
# 9) Terminar.

print('Consecionario Multimarca!')
listado_de_autos={1 : {'Marca': 'vw', 'Modelo': 'vento', 'Año': '2015', 'Precio': 1000, 'Reservado': False}}
auto = {}
salir = False

def mostrar_auto(id , dic):
    print('ID: ', id)
    for x,y in dic[id].items():
        print(x,':',y)

def mostrar_todos(dic):
    for x,y in dic.items():
        print(f'ID:{x} - Marca/Modelo:', y['Marca'] , y['Modelo'] )

def mostrar_precios(dic):
    for x,y in dic.items():
        print(f'ID:{x} - Marca/Modelo:', y['Marca'] , y['Modelo'] , f'(${y.get("Precio")})' )

def mostrar_reservados(dic):
    for x,y in dic.items():
        if y['Reservado'] == True:
            print(f'ID:{x} - Marca/Modelo:', y['Marca'] , y['Modelo'] )

def mostrar_completo(dic , id):
    for x,y in dic[id].items():
        print(x,':' , y )

print('1)Agregar un nuevo auto al inventario' , '2)Eliminar un auto del inventario por ID.' ,'3)Mostrar un auto del inventario por ID.', '4)Mostrar el listado de todos los IDs y la marca/modelo del auto que corresponde a ese ID' , '5)Mostrar el listado de todos los IDs y el modelo y precio ordenado en orden creciente.','6)Informe total autos cargados en el inventario.','7)Marcar un auto como reservado por ID' , '8)Mostrar el listado de todos los IDs y modelos que hayan sido marcados como reservados.' , '9)terminar' , sep='\n'  )

while salir == False:
    num = int(input('Ingrese una opcion: '))

    if num == 1:
        print('Ingresar auto nuevo')
        id = int(input('Ingrese un ID: '))
        for x in listado_de_autos:
            if x == id:
                print('Ya existe ese ID')
                id = input('Ingrese otro ID:')  
        brand = input('Ingrese la marca: ')
        model = input('Ingrese el modelo: ')
        year = input('Ingrese el ano de fabricacion: ')
        price = int(input('precio: '))
        reservation = input('Esta reservado s/n: ')
        if (reservation.lower() == 's'):
            reservation = True
        else:
            reservation = False    
        auto['Marca'] = brand.title()
        auto['Modelo'] = model.title()
        auto['Año'] = year
        auto['Precio'] = price
        auto['Reservado'] = reservation
        listado_de_autos[id] = auto
        mostrar_completo(listado_de_autos , id)
        
    elif num == 2:
       print('eliminar auto del inventario!')
       erase_id = int(input('Ingrese el ID a borrar: '))
       for x in listado_de_autos:
            if erase_id == x:
                print('El ID seleccionado contiene lo siguente: ',listado_de_autos[erase_id])
                valor = (input('Esta seguro que desea eliminarlo s/n?: '))
                confirm = bool('s' == valor.lower())
                if confirm == True:
                    listado_de_autos.pop(erase_id)
                    print('ID eliminado')

            else:
                print('El ID no existe!') 
            break
    
    elif num == 3:
        id = int(input('Ingrese el ID a buscar: '))
        mostrar_auto(id ,listado_de_autos)

    elif num == 4:
        mostrar_todos(listado_de_autos)

    elif num == 5:
        mostrar_precios(listado_de_autos)

    elif num == 6:
        print(f'Hay cargados {len(listado_de_autos)} autos')    

    elif num == 7:
        id = int(input('Ingrese un ID: '))
        var = listado_de_autos[id]['Reservado']
        if var == True:
            listado_de_autos[id]['Reservado'] = False
        else:
            listado_de_autos[id]['Reservado'] = True   
        mostrar_completo(listado_de_autos , id)     
   
    elif num == 8:
        mostrar_reservados(listado_de_autos)   
   
    elif num == 9:
        salir = True
        print('Por fin termine el Examen!')
                   