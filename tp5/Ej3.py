# Escribir un programa que almacene las materias de un curso (por ejemplo Matemáticas,
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en
# cada materia, y después las muestre por pantalla con el mensaje En <materia> has sacado
# <nota> donde <materia> es cada una de las asignaturas de la lista y <nota> cada una de las
# correspondientes notas introducidas por el usuario.

materias = ['Matemáticas',
'Física', 'Química', 'Historia' , 'Lengua']
notas = []

for mat in materias:
    nota = int(input(f'Cual es la nota que saco en la siguiente materia {mat}: '))
    notas.append(nota)
for i in range(len(materias)):    
    print(f'En {materias[i]} has sacado {notas[i]}') 
