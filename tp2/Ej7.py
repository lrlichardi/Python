# Escribir un programa que pregunte por consola el precio de un producto en pesos con dos
# decimales y muestre por pantalla el número de euros y el número de céntimos del precio
# introducido.

precioPesos = input("Ingrese el precio del Producto con dos decimales: ")
buscarComa = precioPesos.find(",")
print(buscarComa)
print(f"El prodcuto vale ${precioPesos[0:buscarComa]} con {precioPesos[(buscarComa+1):]} centavos")
