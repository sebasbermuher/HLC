#Imprima el siguiente patrón. Escriba un programa para imprimir el siguiente patrón de inicio usando 
# el bucle for
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

ancho = int(input("Introduce un numero: "))
for x in range(ancho):
    for y in range(0, x + 1):
        print("*", end=" ")
    print()

for x in range(ancho, 0, -1):
    for y in range(0, x- 1):
        print("*", end=" ")
    print()