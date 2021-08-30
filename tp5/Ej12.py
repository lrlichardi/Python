# Escribir un programa que almacene las matrices A y B en dos tuplas y muestre por pantalla
# # su producto.

a = [[1 , 2 , 3 ] ,
     [4 , 5 , 6 ] ]

b = [[1 , 2] , 
     [3 , 4] , 
     [5 , 6]]
print(len(a[0]))     #columnas matriz 1
print(len(a)) #filas matriz 1
print(len(b[0])) # filas matriz 2
suma = 0
matriz_nueva = []
for i in range(len(a)):
    matriz_nueva.append([0]*len(b[0]))



if len(a[0]) == len(b):
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                matriz_nueva[i][j] += a[i][k] * b[k][j]

print(matriz_nueva)           
    

