#Dada una lista de palabras, imprimir las palabras que tienen una letra específica.

listas_palabras = ["latina", "Hola", "lo que sea", "programación", "sarasa"]
letra = "i"

for palabra in listas_palabras:
    if letra in palabra:
        print(palabra)
