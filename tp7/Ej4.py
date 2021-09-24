# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe
# recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se
# invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21% por defecto.

def factura(monto ,iva = 21):
    total =  monto*((iva/100)+1)
    return total

print(factura(1000))