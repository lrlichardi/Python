#  Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
# todos los números impares desde 1 hasta ese número separados por comas.

num = int(input('Ingrese un numero positivo: '))

i = 1

while (num >= i):
    pares = i%2
    i+=1
    if pares == 0:    
        print(i)
        