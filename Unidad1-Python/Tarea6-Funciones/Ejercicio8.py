#Genere una lista de Python de todos los números pares entre 4 y 30
# Resultado esperado:
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]


def numPares(num):
  comienzo=2
  list=[]
  while comienzo<=num:
    list.append(comienzo*2)
    comienzo+=1
  return list
print(numPares(14))


# Mas sencillo pero sin funcion
# print(list(range(4, 30, 2)))