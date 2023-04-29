#Dada una lista de palabras, imprimir las palabras que tienen una longitud impar.

palabras = ["casa", "ata", "ojo", "perro", "taza", "ratón"]

# Iterar sobre cada palabra en la lista
for palabra in palabras:
    log = len(palabra)
    if log %2 !=0:
        print(palabra)
