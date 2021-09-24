#  Escribir una función que reciba una cantidad una lista de números y devuelva su promedio.
# Hacerlo a su vez para una cantidad indeterminada de números (argumentos) con un
# *argumento.

def promedio(lista):
    sum = 0
    for x in lista:
        sum += x
        p = sum/len(lista)
    return p    

lista1 = [5,5,5,5,5,5]
print(promedio(lista1))        


def promedio1(*lista):
    sum = 0
    for x in lista:
        sum += x
        p = sum/len(lista)
    return p    

print(promedio1(5,5,5,5,5,5))  