# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un
# cilindro usando la primera función.

def area(radio , h=1 ):
    areaCirculo = 3.14*(radio**2)*h
    return areaCirculo

print(area(5 , 5))