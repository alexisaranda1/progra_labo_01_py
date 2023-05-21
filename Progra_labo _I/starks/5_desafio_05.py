
import os
from funciones_desafio import *

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

#1.3

def stark_marvel_app (lista_personajes: list[dict])-> None:
    """
    Toma una lista de diccionarios que representan personajes de Marvel y
    proporciona un menú de opciones para realizar varios cálculos y operaciones en los datos.
    parametro: 
        -lista_personajes: Una lista de diccionarios donde cada diccionario representa un personaje.
    retorno: 
        -None: la funcion no retorna ningun valor.
    """
    stark_normalizar_datos(lista_personajes)

    while True:
        opcion = stark_menu_principal_desafio_5()
        match opcion:
            case "A":
                stark_guardar_heroe_genero(lista_personajes, 'M')
            case "B":
                stark_guardar_heroe_genero(lista_personajes, 'F')
            case "C":
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "maximo" , "altura", "M")
            case "D":
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "maximo" , "altura", "F")
            case "E":
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,"minimo" , "altura", "M")
            case "F":
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,"minimo" , "altura", "F")
            case "G":
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes, "M")
            case "H":
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes, "F")
            case "I":
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "maximo" , "altura", "M")
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "maximo" , "altura", "F")
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,"minimo" , "altura", "M")
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,"minimo" , "altura", "F")
            case "J":
                stark_calcular_cantidad_por_tipo(lista_personajes,"color_ojos")
            case "K":
                stark_calcular_cantidad_por_tipo(lista_personajes, "color_pelo")
            case "L":
                stark_calcular_cantidad_por_tipo(lista_personajes, "inteligencia")
                print("L")      
            case "M":
                stark_listar_heroes_por_dato(lista_personajes, "color_ojos" )
                print("M")
            case "N":
                stark_listar_heroes_por_dato(lista_personajes, "color_pelo" )
                print("N")                    
            case "O":
                stark_listar_heroes_por_dato(lista_personajes, "inteligencia" )
                print(("O"))
            case "Z":
                print("salio!")
                break
            case _:
                print("¡opción incorrecta!.")
    


ruta = r"C:\Users\Axex Shop\Desktop\progra_labo_01\progra_labo_01_py\Progra_labo _I\starks\data_stark.json"
lista_personajes = leer_archivo(ruta)

stark_marvel_app(lista_personajes)