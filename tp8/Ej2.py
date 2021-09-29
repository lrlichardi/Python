#2) Escribir una función que reciba otra función (cuadrado, cubo y factorial) y una lista, y
#devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de
#la lista

import math
lista = []
def aplicador_de_formulas(func , list):
    for x in list:
        func(x)
    print(lista)

def formulas(x):
    cuadrado = int(math.pow(x , 2))
    lista.append(cuadrado)
    cubo = int(math.pow(x , 3))
    lista.append(cubo)
    factor = math.factorial(x)
    lista.append(factor)
    return lista

lista_Prueba = [1, 3, 2 , 5 , 7 , 8 ]

aplicador_de_formulas(formulas , lista_Prueba)