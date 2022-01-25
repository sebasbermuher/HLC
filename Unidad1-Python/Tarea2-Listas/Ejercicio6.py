#Eliminar cadenas vacías de la lista de cadenas
# Dado:
# lista = ["Chema", "", "Juan Diego", "Diana", "", "Alejandro"]
# Resultado:
# ["Chema", "Juan Diego", "Diana", "Alejandro"]

lista = ["Chema", "", "Juan Diego", "Diana", "", "Alejandro"]
listaLimpia = set(lista) #pasamos la cadena a un conjunto(set)
listaLimpia.remove("")
print(listaLimpia)