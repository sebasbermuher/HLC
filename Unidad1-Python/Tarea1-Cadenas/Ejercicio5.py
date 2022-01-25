#Cuente todas las minúsculas, mayúsculas, dígitos y símbolos especiales de una cadena determinada
#str1 = "C@#he26ma^&Du5ran"
#Resultado esperado :
# Recuentos totales de caracteres, dígitos y símbolos 
# Caracteres = 10 
# Dígitos = 3 
# Símbolo = 4
str1 = "C@#he26ma^&Du5ran"
caracteres = 0
digitos = 0
simbolos = 0

for x in str1:
    if x.isalpha():
        caracteres += 1
    elif x.isdigit():
        digitos += 1
    else:
        simbolos += 1

print("Carácteres:", caracteres)
print("Dígitos:", digitos)
print("Símbolos", simbolos)