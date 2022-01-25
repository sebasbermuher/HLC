#Compruebe si todos los elementos de la siguiente tupla son iguales
# tupla = (45, 45, 45, 45)
# Resultado:
# True

tupla = (45, 45, 45, 45)

print(all(x==45 for x in tupla))