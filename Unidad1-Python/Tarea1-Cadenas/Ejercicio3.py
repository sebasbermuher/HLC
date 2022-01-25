#Dadas dos cadenas, s1 y s2 devuelven una nueva cadena compuesta por el primer, el medio y el 
# último carácter de cada cadena de entrada
#s1 = "Chema"
# s2 = "Duran"
# Resultado: CDeran

s1="Chema"
s2="Duran"

s3 = round(len(s1) / 2)
s4 = round(len(s2) / 2)

print(s1[0:1] + s2[0:1] + s1[s3:s3 + 1] + s2[s4:s4 + 1] + s1[len(s1) - 1:] + s2[len(s2) - 1:])
