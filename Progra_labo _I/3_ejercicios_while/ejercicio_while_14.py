#Dada una cadena de texto, imprimir la cantidad de veces que aparece 
# una letra específica en la cadena.

cadena = "Hola, ¿cómo estás?"

caracter = input("ingrese una letra : ")

i = 0

contador_letra = 0 

while i < len(cadena) :
    
    if cadena[i] == caracter:
        contador_letra += 1 
    i += 1
        
        
print('la cantidad de veces que aparece la letra: "{0}" es {1} '
      .format(caracter, contador_letra))
        

