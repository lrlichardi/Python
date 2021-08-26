# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
# pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
# Ej: 13/04/2021 >>>>> 13 de abril de 2021

mes_numeros = { 
    1:'enero',
    2:'febrero',
    3:'marzo',
    4:'abril',
    5:'mayo',
    6:'junio',
    7:'julio',
    8:'agosto',
    9:'septimbre',
    10:'octubre',
    11:'noviembre',
    12:'diciembre'
}

fecha = input('Ingrese una fecha de formato dd/mm/aaaa: ')
mes = int(fecha[3:5])
print(f'{fecha[0:2]} de {mes_numeros.get(mes)} de {fecha[6:10]} ')
