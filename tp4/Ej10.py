# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un
# número primo o no.

num = int(input('Ingrese un numero entero: '))
i = 2

while (num % i != 0):
    i += 1
if num == i:
    print('Numero primo:', num )
else:
    print('Numero NO primo:', num )