#6) Escribir una función que calcule el módulo de un vector.

import math

def modulo_vector(x,y):
    value1 = (x[1] - x[0])**2
    value2 = (y[1] - y[0])**2
    return math.sqrt(value1 + value2)


print(modulo_vector((5,10),(1,5)))