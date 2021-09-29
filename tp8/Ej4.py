#4) Escribir una función reciba una lista de notas y devuelva la lista de calificaciones
#correspondientes a esas notas. Para notas mayores o iguales a 6 devolverá “aprobado” y para
#menores un “desaprobado”


def autocorrector_de_notas(list):
    lista = []
    for x in list:
        if x >= 6:
            lista.append('Aprobado')
        else:
            lista.append('Desaprobado')   
    return lista         


listita = [5 , 8 , 10 , 1 , 2 , 6 , 7 , 10]
print(autocorrector_de_notas(listita))