#Convierta un número decimal en octal usando print() con formato de salida.
#Dado: num = 8
#Resultado: El número octal del número decimal 8 es 10

num = int (input("Introduce un numero y te lo paso a octal: "))
print("%o"% num)
#Otra forma mas compacta
print(f"{num:o}")