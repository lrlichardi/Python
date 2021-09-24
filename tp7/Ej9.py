# Escribir una función que convierta un número decimal en binario y otra que convierta un
# número binario en decimal.

def conversorBinario(num):
    lista = []
    while num != 0:
        resto = num%2
        lista.append(resto)
        num = num // 2
        lista.reverse()
    for x in lista:
        print(x , end='')
       

# conversorBinario(100)

def conversorDecimal(num):
    decimal = []
    
    for x in str(num):
        decimal.append(x)
    decimal.reverse()
    sum = 0
    for x in range(len(decimal)-1 , -1 , -1): 
        sum += int(decimal[x])*(2**x)
        
    return sum    
        
            

print(conversorDecimal(1111))    