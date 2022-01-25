#Invierta la siguiente tupla
# tupla = (10, 20, 30, 40, 50)
# Resultado:
# (50, 40, 30, 20, 10)

def Reverse(tupla): 
    nueva_tupla = tupla[::-1] 
    return nueva_tupla 
      
tupla= (10, 20, 30, 40, 50)
print(Reverse(tupla)) 
