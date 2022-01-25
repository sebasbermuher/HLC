#Escriba un programa para crear una función recursiva para calcular la suma de números del 0 al 10.
# Una función recursiva es una función que se llama a sí misma una y otra vez.
# Resultado:
# 55

def sumaCeroDiez(num):
    if num:
        return num + sumaCeroDiez(num-1)
    else:
        return 0

resultado = sumaCeroDiez(10)
print(resultado)