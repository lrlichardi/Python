# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre
# por pantalla su producto escalar.

x = [ 1 , 2 , 3]
y = [-1 , 0 , 2]
suma = 0

for i in range(len(x)):
   suma += x[i] * y[i]
print(suma) 
