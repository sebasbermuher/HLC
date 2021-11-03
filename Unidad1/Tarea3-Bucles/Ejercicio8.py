#Imprima la lista en orden inverso usando un bucle
# Dado:
# lista = [10, 20, 30, 40, 50]
# Resultado:
# 50
# 40
# 30
# 20
# 10

lista = [10, 20, 30, 40, 50]

for i in range(len(lista)-1, -1, -1):
    print(lista[i])
    
    
#OTRA FORMA
#lista2 = reversed(lista)
#for i in lista2:
#    print(i)