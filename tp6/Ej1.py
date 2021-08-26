# Escribir un programa que guarde en una variable el diccionario {'Peso': '$','Euro':'€',
# 'Dolar':'U$D', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje
# de aviso si la divisa no está en el diccionario.


divisas = {'Peso': '$','Euro':'€','Dolar':'U$D', 'Yen':'¥'}

moneda = input('Ingrese una divisa!: ')

print(divisas.get(moneda.capitalize() , 'No existe en este diccionario'))