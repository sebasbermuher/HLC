#Escriba un programa para imprimir el siguiente patrón numérico usando un bucle.
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

altura = int(input("Introduce la altura del triangulo: "))
for x in range(1, altura+1, 1):
    for y in range(1, x+1, 1):
        print(y, end=" ")
    print("")
    