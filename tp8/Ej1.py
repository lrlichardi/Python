# Escribir una función que simule una calculadora científica que permita calcular el seno,
# #coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario un
# #número “n” y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al
# #valor “n” introducido y el resultado de aplicar la función a esos enteros.

from math import cos, log , sin, tan , exp

def calculadora(n , func):
    print('si aca toy')
    for x in range(1 , n+1):
        print(func(x))

def funciones(funcion):
    func = {'cos' : cos , 'sen' : sin , 'tan' : tan , 'exp' : exp , 'log' : log}
    return func[funcion]

numero = int(input('Ingrese un numero: '))
funcion_input = input('Ingrese la funcion que desea calcular(sen ,cos , tan , log , exp): ')

print(calculadora(numero,funciones(funcion_input)))