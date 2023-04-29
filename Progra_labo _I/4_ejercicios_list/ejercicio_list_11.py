#Crea una lista de palabras y pide al usuario que ingrese una palabra. 
# Luego, muestra todas las palabras de la lista que tienen
# la misma longitud que la palabra ingresada.

lista_palabras = ["lo que sea", "Mascotas", "teclas", "no sé", "Ella"]

palabra_ingresada = input("ingrese una palabra: ")

for palabra in lista_palabras:
    if len(palabra_ingresada) ==  len(palabra):
        print(palabra)
