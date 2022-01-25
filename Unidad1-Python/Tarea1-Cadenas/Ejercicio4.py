#Dada una cadena de entrada con la combinación de mayúsculas y minúsculas,organice los caracteres de tal
# manera que todas las letras minúsculas deben ir primero.
# str1 = ChEmaDUraN
# Resultado: hmaraCEDUN

s1="ChEmaDUraN"
print(s1[1:2] + s1[3:5] + s1[7:9] + s1[0:1] + s1[2:3] + s1[5:7] + s1[9:])
