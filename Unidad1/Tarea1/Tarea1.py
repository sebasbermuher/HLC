#Dada una cadena de longitud impar mayor que 7, devuelva una nueva cadena formada 
# por los tres caracteres del medio de una cadena determinada

string = input("Introduce una cadena mayor de 7 caracteres e impar: ")
mitad = round(len(string) / 2 - 1)
impar = len(string) % 2

if len(string) >= 7 and impar!= 0:
    print(string[mitad:mitad + 3])