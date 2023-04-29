#Dada una lista de palabras, imprimir todas las palabras que tengan una
# longitud mayor a 5 caracteres.
palabras = ["gato", "perro", "casapop", "jardín", "computadora", "sol", "libro",
            "mesa", "silla", "lápiz"]

i = 0

while i < len(palabras):
    if len(palabras[i]) > 5:
        print(palabras[i]) 
    i += 1

