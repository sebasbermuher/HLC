#Crea una función interna para calcular la suma de la siguiente manera
# Cree una función externa que acepte dos parámetros a y b
# Cree una función interna dentro de una función externa que calculará la suma de a y b
# Por último, una función externa agregará 5 y lo devolverá

def funcion(a, b):
    def funcion2(a,b):
        return a+b
    agregarCinco = funcion2(a, b)
    return agregarCinco+5

resultado = funcion(20, 25)
print(resultado)