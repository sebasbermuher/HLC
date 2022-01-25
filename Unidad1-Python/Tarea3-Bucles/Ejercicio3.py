#Escriba un programa para aceptar un número de un usuario y calcular la suma de todos los números 
# desde 1 hasta un número dado. Por ejemplo, si el usuario ingresó 10, la salida 
# debería ser 55 (1+2+3+4+5+6+7+8+9+10)

# Resultado:
# Ingrese el número: 10
# La suma es: 55

num = int(input("Introduce un numero "))
x = 1
y = 0

while x <= num:
  y = y + x
  x += 1
  
print (y)