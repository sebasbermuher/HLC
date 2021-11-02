#Crea un diccionario de datos para la lista de todos los empleados cuyas claves sean los empleados, 
# y los datos, los datos por defecto que se dan a continuación. Con el diccionario resultado, 
# accede a sus datos e imprímelos.
# Dado:
# empleados = ['Rodogiro', 'Atacuerdo', 'Caminancio']
# datos = {"puesto": 'Desarrollador Facebook', "salario": 12000}
# Resultado:
# {'Rodogiro': {'puesto': 'Desarrollador Facebook', 'salario': 12000}, 
# 'Atacuerdo': {'puesto': 'Desarrollador Facebook', 'salario': 12000}, 
# 'Caminancio': {'puesto': 'Desarrollador Facebook', 'salario': 12000}}

empleados = ['Rodogiro', 'Atacuerdo', 'Caminancio']
datos = {"puesto": 'Desarrollador Facebook', "salario": 12000}

diccionario = dict.fromkeys(empleados,datos)
print(diccionario)