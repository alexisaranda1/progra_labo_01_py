#Dada una lista de palabras, imprimir las palabras que tienen una letra mayúscula

palabras = ['Hola', 'mundo', 'python', 'Ejemplo', 'lista', 'Mayúsculas']

for palabra in palabras:
    if palabra.isupper():
        print(palabra)
    else:
        for letra in palabra:
            if letra.isupper():
                print(palabra)
                break
