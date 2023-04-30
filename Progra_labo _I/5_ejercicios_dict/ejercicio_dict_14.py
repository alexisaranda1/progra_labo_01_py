

#Crea un diccionario que contenga el nombre como clave y
# el puntaje como valor de varios jugadores en un juego.
# Luego, pedirle al usuario el nombre del jugador y
# nuevo puntaje y actualizar el valor correspondiente en el diccionario.

jugadores = {
    "Juan": 100,
    "Pedro": 85,
    "María": 120,
    "Ana": 95,
    "Luis": 110
}


nombre_jugador = input("Ingresa el nombre del jugador: ")
nuevo_puntaje = int(input("Ingresa el nuevo puntaje para el jugador {0}: "
                          .format(nombre_jugador)))

jugadores[nombre_jugador] = nuevo_puntaje

print("El puntaje actualizado del jugador {} es: {}".format(nombre_jugador, 
                                            jugadores[nombre_jugador]))
