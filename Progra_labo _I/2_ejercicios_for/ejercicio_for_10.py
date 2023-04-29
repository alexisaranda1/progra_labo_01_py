#Dada una lista de palabras, imprimir las palabras que comienzan
# y terminan con la misma letra.

# Crear una lista de palabras
palabras = ["casa", "ata", "ojo", "perro", "taza", "ratón"]

# Iterar sobre cada palabra en la lista
for palabra in palabras:
    # Verificar si la primera y la última letra son iguales
    if palabra[0] == palabra[-1]:
        # Imprimir la palabra si cumple con la condición
        print(palabra)
