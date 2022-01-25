#Escriba un programa para crear una función que tome dos argumentos, nombre y edad, e imprima 
# su valor.

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

def nombreEdad(nombre,edad):
  print("Mi nombre es",nombre ,"y mi tengo " , edad,"años")

nombreEdad(nombre,edad)