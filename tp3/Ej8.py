# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
# ingredientes para cada tipo de pizza aparecen a continuación.
#  Ingredientes vegetarianos: Pimiento y tofu.
#  Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función
# de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se
# puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los
# ingredientes que lleva.

tipo = input('Que tipo de pizza desea? vegetarianas y no vegetarianas?')

if tipo =='vegetarianas':
    ingrediente =  input("""Con que ingrediente lo desea? solo puede elegir uno!
    Pimiento
    Tofu
    Escriba aca su ingrediente: """)
    if ingrediente.lower() == 'pimiento':
        print(f"Usted eligio una pizza {tipo.upper()} con el siguiente ingrediente {ingrediente.upper()}")
    elif ingrediente.lower() == 'tofu':
        print(f"Usted eligio una pizza {tipo.upper()} con el siguiente ingrediente {ingrediente.upper()}")
    else:
         print('La opcion elegida no existe!')   
     
elif tipo ==  'no vegetarianas':
    ingrediente =  input("""Con que ingrediente lo desea? solo puede elegir uno!
    Peperoni
    Jamon
    Salmon
    Escriba aca su ingrediente: """)
    if ingrediente.lower() == 'peperoni':
        print(f"Usted eligio una pizza {tipo.upper()} con el siguiente ingrediente {ingrediente.upper()}")
    elif ingrediente.lower() == 'jamon':
        print(f"Usted eligio una pizza {tipo.upper()} con el siguiente ingrediente {ingrediente.upper()}")
    elif ingrediente.lower() == 'salmon':
        print(f"Usted eligio una pizza {tipo.upper()} con el siguiente ingrediente {ingrediente.upper()}")    
    else:
         print('La opcion elegida no existe!')   
else:
    print('La opcion elegida no existe!')    