#Invertir un número entero dado
# Dado:
# 76542
# Resultado:
# 24567

num = int(input("Introduce un numero: "))
num_invertido = 0

while num > 0:
    div = num % 10
    num_invertido = (num_invertido * 10) + div
    num = num // 10
print(num_invertido)