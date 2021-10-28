#Concatenar dos listas por índice
# Dado:
# lista1 = ["M", "nom", "e", "Che"]
# lista2 = ["i", "bre", "s", "ma"]
# Resultado:
# ['Mi nombre es Chema']

lista1 = ["M", "nom", "e", "Che"]
lista2 = ["i", "bre", "s", "ma"]
cadena = ""
for i in range(len(lista1)):
    cadena += (lista1[i] + lista2[i]) + " "
print(cadena)