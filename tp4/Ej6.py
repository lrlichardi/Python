# Escribir un programa que pida al usuario un número entero y muestre por pantalla un
# triángulo rectángulo como el de más abajo (para n=5), de altura el número introducido.

n = int(input('Ingrese un numero: '))

for i in range(n+1):
    print('*' * i, end='\n')