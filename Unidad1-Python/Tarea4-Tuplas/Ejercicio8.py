#Ordenar una tupla de tuplas por segundo elemento
# tupla = (('a', 23),('b', 37),('c', 11), ('d',29))
# Resultado:
# (('c', 11), ('a', 23), ('d', 29), ('b', 37))

tupla = (('a', 23),('b', 37),('c', 11), ('d',29))

lista = list(tupla) #paso a la lista los datos de la tupla

lista.sort(key = lambda x: x[1]) #ordeno la lista por el segundo elemento

tupla=tuple(lista) #paso a la tupla los datos de la lista (ordenados anteriormente)

print(tupla)