#Busque todas las apariciones de "que" en una cadena dada, independientemente que esté o no en mayúsculas.
# Dado :
# str1 = "Lo que yo te diga. Que la vida es así"
# Resultado:
# El recuento de 'que' es: 2

s1 = input("Introduce una cadena: ")
count_s1 = s1.lower().count("que")
print(count_s1)