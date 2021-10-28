#Aplicar formato a las variables mediante el método string.format(). 
#Escriba un programa para usar el método string.format() para formatear las 
#siguientes tres variables según la salida esperada.
#Dado:
#totalMoney = 1000
#quantity = 3
#price = 450
#Resultado: Tengo 1000 euros para comprar 3 tarjetas gráficas por 450,00 dólares.

cantidad = 3
dinero = 1000
precio = 450
resultado = "Tengo {1} euros para comprar {0} tarjetas gráficas por {2:.2f} dolares"

print(resultado.format(cantidad, dinero, precio))

#forma corta y mas compacto
#print(f"Tengo {dinero} euros para comprar {cantidad} tarjetas gráficas por {precio:.2f} dolares")