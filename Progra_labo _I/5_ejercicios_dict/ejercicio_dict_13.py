#Crea un diccionario que contenga el nombre y el nivel de dificultad 
# de varios juegos de mesa. 

# Luego, pedirle al usuario un nivel de dificultad,
# buscar los que coinciden e imprimir sus nombres

juegos_mesa = {
    "Ajedrez": "Difícil",
    "Dominó": "Fácil",
    "Risk": "Moderado",
    "Monopoly": "Moderado",
    "Scrabble": "Moderado"
}

nivel_dificultad = input("ingrese el nivel de dicultad: ")

for clave, valor in juegos_mesa.items():
    
    if nivel_dificultad == valor:
        print("Nopmbre : {0}".format(clave))