# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(num):
    for x in range(1 , num):
        num = num*x 
    return print(num)    

factorial(5)