#Dada una lista de palabras, imprimir la cantidad total de vocales en la lista.

cadena_texto = "Hola, ¿todo bien?"
vocales = "aeiouAEIOU"
contador_vocales = 0

for i in cadena_texto :
    if i in vocales:
        contador_vocales += 1
 
    
print("La cantidad de vocales en la cadena es:", contador_vocales)