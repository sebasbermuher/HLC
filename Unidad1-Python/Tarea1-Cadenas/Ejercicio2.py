#Dadas dos cadenas, s1 y s2, cree una nueva cadena agregando s2 en medio de s1
#s1=Hola // s2=Adios
#Resultado = HoAdiosla

s1="Hola"
s2="Adios"

mitad_s1 = round(len(s1) / 2)

print(s1[0:mitad_s1] + s2 + s1[mitad_s1:])