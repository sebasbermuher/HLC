#Reemplace cada puntuación con # en la siguiente cadena
#Dado :
#str1 = '/*Chema es @profesor & maker!!'
#Resultado:
##Chema es #profesor # maker##

str1 = "/*Chema es @profesor & maker!!"
simbolos = "/*@&!"

for i in range(len(simbolos)):
    str1 = str1.replace(simbolos[i], "#")
print(str1)