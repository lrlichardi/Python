# Escribir un programa que pregunte por consola por los productos de un carro de compras,
# separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

carrito = input("Que desea agregar al carrito escriba de la sgte manera queso,pan,huevo:\n")
print(carrito.replace("," , "\n"))