#Fusionar los siguientes dos diccionarios en uno
# Dado:
# dict1 = {'Diez': 10, 'Veinte': 20, 'Treinta': 30}
# dict2 = {'Treinta': 30, 'Cuarenta': 40, 'Cincuenta': 50}
# Resultado:
# {'Diez': 10, 'Veinte': 20, 'Treinta': 30, 'Cuarenta': 40, 'Cincuenta': 50}

dict1 = {'Diez': 10, 'Veinte': 20, 'Treinta': 30}
dict2 = {'Treinta': 30, 'Cuarenta': 40, 'Cincuenta': 50}

#Metodo update
dict1.update(dict2)
print (dict1)

#Combinando los dos diccionarios
print (dict(dict1, **dict2))