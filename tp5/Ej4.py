# Escribir un programa que pregunte al usuario los números ganadores de la lotería, los
# almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
numeros = []

print('Ingrese los 5 numeros de la loteria')
for i in range(5):
    num = int(input(f'Ingrese su numero {i+1}: '))
    numeros.append(num)

numeros.sort()

print(numeros)
