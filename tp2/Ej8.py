# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
# dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para
# que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha = input("ingrese su cumpleaños en formato dd/mm/aaaa: \n")
print(f"Usted cumple el dia {fecha[0:2]} del mes {fecha[3:5]} del año {fecha[6:10]}") #funciona solo dd/mm/aaaa
dia = fecha.find("/")
mes = fecha.find("/", dia+1)
print(f"Usted cumple el dia {fecha[0:dia]} del mes {fecha[dia+1:mes]} del año {fecha[mes+1:]}") #funciona con cualquier formato de fecha 




