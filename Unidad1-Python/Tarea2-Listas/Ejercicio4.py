#Concatenar dos listas en el siguiente orden
# Dado:
# lista1 = ["Hola ", "toma "]
# lista2 = ["guapo", "señor"]
# Resultado:
# ['Hola guapo', 'Hola señor', 'toma guapo', 'toma señor']

lista1 = ["Hola ", "toma "]
lista2 = ["guapo", "señor"]
cadenaFinal = []

HolaGuapo = lista1[0] + lista2[0]
cadenaFinal.append(HolaGuapo)

HolaSeñor = lista1[0] + lista2[1]
cadenaFinal.append(HolaSeñor)

tomaGuapo = lista1[1] + lista2[0]
cadenaFinal.append(tomaGuapo)

tomaSeñor = lista1[1] + lista2[1]
cadenaFinal.append(tomaSeñor)

print(cadenaFinal)