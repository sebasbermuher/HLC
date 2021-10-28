#Prueba de equilibrio de caracteres de cadena
# Asumiremos que una cadena s1 y s2 está equilibrada si todos los caracteres de s1 están en s2. 
# la posición de los caracteres no importa.

s1 = input("Introduce cadena1: ")
s2 = input("Introduce cadena2: ")
equilibrada = True

for x in s1:
    if s2.count(x) == 0:
        equilibrada = False
        break

print(equilibrada)