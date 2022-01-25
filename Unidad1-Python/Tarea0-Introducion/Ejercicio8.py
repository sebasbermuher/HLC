#Calcula la multiplicación y la suma de dos números. Dados dos números enteros, 
# devuelve su producto sólo si el producto es mayor que 1000, de lo contrario, 
# devuelve su suma.

num1 = input("Introduzca un numero: ")
num2 = input("Introduzca otro número: ")

suma = int(num1) + int(num2)
multiplicacion = int(num1) * int(num2)

if multiplicacion > 1000:
    print(multiplicacion)
else:
    print(suma)