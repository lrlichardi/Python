# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si
# el divisor es cero el programa debe mostrar un error.

num1 = int(input("Ingrese un numero:"))
num2 = int(input("Ingrese otro numero: "))

if num2 != 0:
     print("La division es : " , round(num1/num2 ,2))
else:
     print("No se puede dividi en 0")

