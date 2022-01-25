#Dada una lista, busque el valor 20 en la lista y, si está presente, reemplácelo con 200. 
# Solo actualice la primera aparición de un valor
# Dado:
# lista = [5, 10, 15, 20, 25, 50, 20]
# Resultado:
# lista = [5, 10, 15, 200, 25, 50, 20]

lista = [5, 10, 15, 20, 25, 50, 20]
  
for i in range(len(lista)):
    if lista[i] == 20:
        lista[i] = 200
        break #para que deje de buscar otro 20 y solo cambie el primer 20
print(lista)