# Escribir un programa que cree un diccionario simulando una lista de compras. El programa
# debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida
# terminar. Después se debe mostrar por pantalla la lista de compras ingresada y el precio total
# de todo lo que incluye.

lista = {}
pregunta = 's'

while pregunta == 's':
        articulo = input('Ingrese un articulo: ')
        precio = int(input('Ingrese el valor del articulo en $: '))
        lista[articulo] = precio
        pregunta = input('Desea agregar otro articulo a la lista: s/n? : ')

sum = 0
for n in lista:
    sum += lista.get(n)

for n in lista:
    print(f'{n} ----------- {lista.get(n)}')
print(f'Total ------------ {sum}')    
   
    


