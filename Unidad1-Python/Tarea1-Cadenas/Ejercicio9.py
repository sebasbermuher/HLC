#Dada una cadena, devuelve la suma y el promedio de los dígitos que aparecen en la cadena, 
# ignorando todos los demás caracteres.
# Dado :
# str1 = "Galicia = 78 Andalucia = 83 Canarias = 68 Cataluña = 65"
# Resultado:
# la suma es 294
# el promedio es 73.5

str1 = "Galicia = 78 Andalucia = 83 Canarias = 68 Cataluña = 65"
suma=0
cont=0

for x in str1.split(sep = " "):
    if (x.isdigit()):
        suma += int(x)
        cont += 1
print("la suma es "+str(suma))
print("el promedio es "+str(suma/cont))