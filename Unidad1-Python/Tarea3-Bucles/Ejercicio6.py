#Escriba un programa para contar el número total de dígitos en un número usando un ciclo while. 
# Por ejemplo, el número es 75869, por lo que la salida debería ser 5.

num = int(input("Introduce un numero: "))
numfijo = num
contador = 0
while num != 0:
    num = num // 10
    contador = contador + 1
print("En el numero ", numfijo , " hay ", contador, " dígitos.")

