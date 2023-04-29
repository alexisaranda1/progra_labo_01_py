#Crea una lista con los nombres de tus 3 películas favoritas 
# y luego imprime los elementos en orden inverso 
# (sin utilizar el método reverse())

lista_peliculas = ["the butterfly", "Juegos  del miedo", "chucky"]

for i in range(len(lista_peliculas)-1, -1, -1):
    print(lista_peliculas[i])