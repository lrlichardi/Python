# EJERCICIO 1
print("hola Mundo")

# EJERCICIO 2
saludo = "hola Mundo"
print(saludo)

# EJERCICIO 3
nombre = input("Cual es tu nombre?")
print("hola" , nombre)

# EJERCICIO 4
resultado = ((3+2)/(2*5))**2
print(resultado)

# EJERCICIO 5
print("Calculadora de pago de un dia de trabajo")
horas = int(input("Proporcione el numero de horas trabajadas por dia: "))
pago = int(input("Proporcione el precio de la hora de trabajo: "))
print("El pago por dia es: " ,horas * pago , "pesos") 

# EJERCICIO 6
print("Sumador de numeros de 1 a n numero que usted elija")
n = int(input("Ingrese un numero "))
sum = 0
if n>0: 
     sum = (n*(n+1))/2
     print(sum)
else: 
    print("El numero tiene que ser positivo")


# EJERCICIO 7
print("Sistema para calcular IMC")

peso = float(input("ingrese su peso en kg: "))
altura = float(input("ingrese su altura en metros: "))
imc = peso / altura**2
imc = round(imc,2)
print("Tu índice de masa corporal es" , imc)

# EJERCICIO 8
print("Sistema para calcular el resto y cociente de una division de dos numeros enteros")
n = int(input("ingrese un numero entero "))
m = int(input("ingrese otro numero entero "))
c = n//m
r = n%m
print("El cociente de n/m es c: " , c , "y el resto es r:" , r)

# EJERCICIO 9
print("Sistema para calcular inversiones ")
cantidad = float(input("Cantidad a invertir "))
interesa = float(input("Interes anual "))
años = float(input("Cantidad de años de la inversion "))
print ("La capital obtenido es: " ,round(cantidad*((interesa/100)+1)*años , 2) , "pesos")

# EJERCICIO 10
nombre = input("Ingrese su nombre: ")
n = int(input("Ingrese un numero n de veces que quiera que se repita su nombre: "))
print(nombre * n)