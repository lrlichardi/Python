# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El
# programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el
# cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si
# es mayor de 18 años, $1.000
    
edad = int(input('Ingrese su edad: '))   

if edad < 4:
    print('La entrada para vos es gratis!!!!')
if 4 <= edad <= 18:
    print('Usted de pagar $500 de entrada')
if edad > 18:
    print('Usted debe pagar $1000 de entrada')     
    
    
    
    
    
    
  