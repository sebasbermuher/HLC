# Agregue el elemento 7000 después de 6000 en la siguiente lista
# Dado:
# lista1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Resultado:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

lista1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
lista1[2][2].append(7000)
print(lista1)
