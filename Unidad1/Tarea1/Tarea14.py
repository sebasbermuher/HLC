#Eliminar cadenas vacías de una lista de cadenas

#Dado :
#str_list = ["Chema", "Alejandro", "", "Juan Diego", None, "Diana", ""]
#Resultado esperado :
# lista original
#['Chema', 'Alejandro', '', 'Juan Diego', None, 'Diana', '']
# Después de quitar cadenas vacías
#['Chema', 'Alejandro', 'Juan Diego', 'Diana']

str_list = ["Chema", "Alejandro", "", "Juan Diego", None, "Diana", ""]

print("Lista original:", str_list)

while "" in str_list:
    str_list.remove("")

print("Despues de quitar cadenas vacías:", str_list)