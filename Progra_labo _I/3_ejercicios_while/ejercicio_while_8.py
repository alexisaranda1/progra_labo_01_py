# Dada una cadena de texto, imprimir la cantidad de vocales en la cadena.
texto = "Hola, ¿todo bien?"
vocales = "aeiouAEIOU"

contador_vocales = 0
i = 0

while i < len(texto) :
    letra = texto[i]
    if letra in vocales:
        contador_vocales += 1
    i += 1
    
print("La cantidad de vocales en la cadena es:", contador_vocales)
