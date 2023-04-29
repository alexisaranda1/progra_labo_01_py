#Dada una lista de palabras, imprimir la palabra más larga de la lista.

palabras = ["lo que sea", "Hola", "que?", "ok", "python"]
palabra_mas_larga = ""

for palabra in palabras:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

print("La palabra más larga es: ", palabra_mas_larga)
