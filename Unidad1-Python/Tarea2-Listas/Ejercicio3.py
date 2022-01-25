#Dada una lista de números. Convierte cada elemento de una lista en su cuadrado
# Dado:
# lista = [1, 2, 3, 4, 5, 6, 7]
# Resultado:
# [1, 4, 9, 16, 25, 36, 49]


lista = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(lista)):
    lista[i] = pow(lista[i], 2)
print("El cuadrado de la lista es:",lista)