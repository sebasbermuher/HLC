#Calcule el cubo de todos los números desde 1 hasta un número dado. 
# Escribe un programa para imprimir el cubo de todos los números del 1 al número dado.
# Dado:
# input_number = 6
# Resultado:
# El número actual es: 1 y el cubo es 1
# El número actual es: 2 y el cubo es 8
# El número actual es: 3 y el cubo es 27
# El número actual es: 4 y el cubo es 64
# El número actual es: 5 y el cubo es 125
# El número actual es: 6 y el cubo es 216

num = int(input("Introduce un numero: "))
for x in range(1, num + 1):
    print("El numero actual es:", x, " y el cubo es", (x * x * x))