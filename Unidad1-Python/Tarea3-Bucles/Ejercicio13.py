#Encuentra el factorial de un número dado. Escribe un programa para usar el ciclo para encontrar 
# el factorial de un número dado.
# El factorial (símbolo !) significa que se multiplican todos los números enteros desde el 
# número elegido hasta 1.
# Por ejemplo: calcula el factorial de 5 5! = 5 × 4 × 3 × 2 × 1 = 120
# Resultado:
# 120

num = int(input("Introduce un numero positivo "))
factorial = 1

if num == 0:
    print("El factorial de 0 es 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("El factorial de ",num," es ",factorial)