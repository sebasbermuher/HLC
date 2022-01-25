#Encuentra la suma de la serie hasta n términos. Escribe un programa para calcular la suma de series 
# hasta n términos. Por ejemplo, si n =5 la serie se convertirá en 2 + 22 + 222 + 2222 + 22222 = 24690
# Dado:
# numero de terminos
# n = 5
# Resultado:
# 24690

num = int(input("Introduce un numero: "))
num2serie = 2
aux_suma = 0

for x in range(0,num):
    aux_suma += num2serie
    num2serie = num2serie * 10 + 2
print(aux_suma)