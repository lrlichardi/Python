nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
dni = int(input('Ingrese su documento: '))
licencia = input('Tiene Licencia de conducir si o no escriba: ')
esta_en_lista_negra = True

if edad >= 25 and licencia.lower() == 'si':
        tipolicencia = input('Que tipo de licencia tiene? profesional o comun? ')
        if tipolicencia.lower() == 'comun':
           print('Usted entra en el segmento general por el tipo de licencia')
           segmento = 'Comun'
        elif  tipolicencia.lower() == 'profesional':
            print('Usted entra en el segmento premium por el tipo de licencia')
            segmento = 'Profesional'
        else:
            print('Ingreso un tipo de licencia no valida!')    
        anos = int(input('Escriba los años de experencia en puestos similares: ')) 
        sueldo = int(input('Cual es el sueldo prentedido? '))   
        if anos == 0 and 0 < sueldo < 40000:
             print('Usted califica')
             experencia = 'inexperto'
        elif 0 <= anos < 2 and 0 < sueldo < 50000: 
            print('Usted califica')
            experencia = 'Conocedor'
        elif 2 <= anos < 5 and 0 < sueldo < 60000: 
            print('Usted califica')
            experencia = 'Experimentado'
        elif anos >= 5  and 0 < sueldo < 70000: 
            print('Usted califica')  
            experencia = 'Experto'
        else:
            print('No clasifica')                  
        if dni == 33697050 or dni == 46039485  or dni == 38495069:
            print('No aplica a la busqueda Muchas Gracias')  
        else:
            esta_en_lista_negra = False
            

else:
    print('No aplica a la busqueda Muchas Gracias')   

print(f"""
Gracias por postularte, {nombre}!
Segmento: {segmento}
Experiencia: {experencia}
Rem pretendida: ${sueldo}
Nos vamos a estar comunicando con vos!
""")