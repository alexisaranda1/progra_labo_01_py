#Crea una lista de palabras y muestra las palabras que tienen más de 5 letras.

lista_palabras = ["lo que sea", "Mascotas", "teclas", "no sé", "Ella"]
 
for palabra in lista_palabras:
    if len(palabra) > 5:
        print("la palabra ({})  tiene más de 5 letras".format(palabra))

