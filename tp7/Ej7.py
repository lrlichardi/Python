# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista
# con sus cuadrados. Idem anterior, con lista y con *arg.

def cuadrados(lista):
    listaCuadrada = []
    for x in lista:
        listaCuadrada.append((x*x))
    return listaCuadrada    

numeros = [ 1 ,2 , 3, 4 ,5]
print(cuadrados(numeros))    

def cuadrados1(*lista):
    listaCuadrada = []
    for x in lista:
        listaCuadrada.append((x*x))
    return listaCuadrada    

print(cuadrados1(1 ,2 , 3, 4 ,5,6,7,8))    