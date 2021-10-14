#Divida una cadena dada con guiones en varias subcadenas y muestre cada subcadena.
#Dado :
#str1 = Chema-es-un-profesor
#Resultado:

#Chema
#es
#un
#profesor

str1 = "Chema-es-un-profesor"

for i in str1.split("-"):
    print(i)