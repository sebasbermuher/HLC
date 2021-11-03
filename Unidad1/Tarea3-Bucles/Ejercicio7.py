#Escriba un programa para usar el bucle for para imprimir el siguiente patrón numérico inverso:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

num = 5
num2 = 5
for x in range(0,num+1):
    for y in range(num2-x,0,-1):
        print(y,end=" ")
    print()