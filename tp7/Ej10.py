# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario
# generado con la función anterior y devuelva una tupla con la palabra más repetida y su
# frecuencia.

diccionario = {}
def cadena_caracteres(text):
    cadena = text.split()
    for x in cadena:
        sum = 0
        for y in range(len(cadena)):  
            if x == cadena[y]:
                sum += 1
        diccionario[x] = sum        
            
          
    return diccionario    
cadena_caracteres("hola hola que que que haces jaja")    

def formador_tupla(dic):
    may = 0
    for x in diccionario:
        if may < diccionario[x]:
            may = diccionario[x]
            tupla = (x , may)

    print(tupla[0] , ':' , tupla[1])           


        
        

formador_tupla(diccionario)

