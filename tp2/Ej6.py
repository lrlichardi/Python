correo = input("Ingrese su correo electronico: ")
buscaArroba = correo.find("@")
newcorreo = correo.replace(correo[buscaArroba:],"@idetel.com.ar")
print(newcorreo)
