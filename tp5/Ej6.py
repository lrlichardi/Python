# Escribir un programa que almacene las materias de un curso (por ejemplo Matemáticas,
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en
# cada materia y elimine de la lista las materias aprobadas. Al final el programa debe mostrar
# por pantalla las materias que el usuario tiene que recursar.

materias = ['Matemáticas',
'Física', 'Química', 'Historia' , 'Lengua']
notas = []
mate = []
notasf = []
for mat in materias:
    nota = int(input(f'Cual es la nota que saco en la siguiente materia {mat}: '))
    notas.append(nota)

for i in range(len(materias)): 
    if notas[i] < 4:
       mate.append(materias[i])
       notasf.append(notas[i])  

for i in range(len(mate)):  
    print(f'En {mate[i]} has sacado {notasf[i]}') 