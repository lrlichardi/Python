#  Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese
# número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje
# informando de ello.

frutas = {'banana': 120 , 'manzana' : 150 , 'pera': 80 , 'naranja' : 50}

fruta_elegida = input('Ingrese una fruta: ')
kg = int(input('Ingrese el numero de kg que desea: '))

precio = frutas.get(fruta_elegida , f'No se encontro esa fruta {fruta_elegida}')
print(f'El kg de {fruta_elegida} cuesta {precio} por lo tanto usted debe abonar por los {kg} kilos la suma de {precio * kg}')
