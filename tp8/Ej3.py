#3) Escribir una función que reciba una frase y devuelva un diccionario con las palabras que
#contiene y su longitud.

def separador(text):
    diccionario = {}
    text_array = text.split()
    for x in text_array:
        diccionario[x] = len(x)
    return diccionario

print(separador('hola que haces todo bien que onda papaquee'))    
