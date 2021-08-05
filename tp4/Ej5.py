# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
# número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura
# la inversión.

cantidad = int(input('Ingrese la suma a invertir: '))
interes = int(input('Cual es el interes anual: '))
anos = int(input('Ingrese los anos que dura la inversion: '))
capital = cantidad
for i in range(anos):
    capital = capital + (capital * (interes/100))
    print(f'El ano {i+1} el capital obtenido sera {round(capital , 2)} ')