#Dadas dos cadenas, s1 y s2, cree una cadena mixta usando las siguientes reglas
# Nota : cree una tercera cadena hecha del primer carácter de s1, luego el último carácter de s2, 
# Siguiente, el segundo carácter de s1 y el segundo último carácter de s2, y así sucesivamente. 
# Los caracteres sobrantes van al final del resultado.
# Dado:
# s1 = "Abc"
# s2 = "Xyz"
# Resultado esperado:
# AzbycX

s1 = "Abc"
s2 = "Xyz"
s3 = ""

for x in range(len(s1)):
    s3 += s1[x]
    s3 += s2[(x*-1-1)]
    
print(s3)