#Dada una cadena de entrada, cuente las apariciones de todos los caracteres dentro de una cadena
# Dado :
# str1 = "Apple"
# Resultado:
# {'A': 1, 'p': 2, 'l': 1, 'e': 1}

str1 = input("Introduce una cadena: ")
cont_caracter = {}

for x in str1:
    cont_caracter[x] = str1.count(x)
print(cont_caracter)