#5) Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y
#devuelva otro diccionario con las asignaturas en mayúsculas y las notas en formato texto.
#Ej: {matemática: 9} seria {MATEMATICA: Nueve}

dic_apoyo = { 1:'Uno' , 2:'Dos' , 3:'Tres' , 4:'Cuatro' , 5:'Cinco' , 6:'Seis' , 7:'Siete' , 8:'Ocho' , 9:'Nueve' , 10:'Diez'}
def corrector(dic):
    dic_modificado = {}
    for x in dic:
        nota = dic1[x]
        nota_letra = dic_apoyo[nota]
        dic_modificado[x.upper()] = nota_letra
    return dic_modificado


dic1 = {'matematicas': 1 , 'lengua':4 , 'fisica':4 , 'computacion':10}
print(corrector(dic1))