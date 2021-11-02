#Eliminar un conjunto de claves de un diccionario
# Dado:
# diccionario = {
    # "nombre": "Pikolo",
    # "edad": 28,
    # "salario": 8000,
    # "planeta": "Namek"
    # }
# keysToRemove = ["nombre", "salario"]
# Resultado:
# {'planeta': 'Namek', 'edad': 28}

diccionario = {
    "nombre": "Pikolo",
    "edad": 28,
    "salario": 8000,
    "planeta": "Namek"
    }

keysToRemove = ["nombre", "salario"]

diccionario2 = {x: diccionario[x] for x in diccionario.keys() - keysToRemove}
print(diccionario2)

#OTRA FORMA
#[diccionario.pop(key) for key in ['nombre', 'salario']]
#print(diccionario)
