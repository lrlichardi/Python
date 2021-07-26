# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla que % de
# impuestos le corresponde y cuando debe pagar.
# Nota: pago = renta * %impuesto

renta = int(input('Escriba su renta anual? \n'))

if renta < 10000:
    print('Usted debe pagar un 5% de impuesto , impuesto:  ' , renta * 0.05)
if  10000 <= renta < 20000:    
    print('Usted debe pagar un 15% de impuesto , impuesto:' , renta * 0.15)
if 20000 <= renta < 35000:    
    print('Usted debe pagar un 20% de impuesto , impuesto:' , renta * 0.2)
if 35000 <= renta < 60000:    
    print('Usted debe pagar un 30% de impuesto , impuesto:' , renta * 0.3)
if renta >= 60000:   
    print('Usted debe pagar un 45% de impuesto , impuesto:' , renta * 0.45)            
    