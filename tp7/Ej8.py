# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule
# el mínimo común múltiplo.
   
def maximo(a, b):
    x = 0
    while b != 0:
        x = b
        b = a % b
        a = x
    return a
   
print(maximo(120 , 200 ))

def max(a, b):
    if b == 0:
        return a
    return maximo(b, a % b)

def minimo(a, b):
    return (a*b)/max(a,b)

print(maximo(120 , 200 ))
print(max(120 , 200))
print(minimo(120 , 200))