#Dada una lista, elimine todas las ocurrencias de 20 de la lista
# Dado:
# lista = [5, 20, 15, 20, 25, 50, 20]
# Resultado:
# [5, 15, 25, 50]

lista = [5, 20, 15, 20, 25, 50, 20]
listaFinal = set(lista)
listaFinal.remove(20)
print(listaFinal)