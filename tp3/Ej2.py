# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por
# el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas

passwordGuardado = "lucas"
password = input("Ingrese su contraseña!\n")

if passwordGuardado == password.lower():
    print("Hola LUCAS! ")
else:
    print("CONTRASEÑA INCORRECTA")