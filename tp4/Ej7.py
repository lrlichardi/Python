# Escribir un programa que pida un número entero y muestra la tabla de multiplicar de ese
# número, ej: (n = 6)

num = int(input('Ingrese un numero!: '))

for i in range(0 , 10):
    print(f'{num} x {i} = {num*i}')