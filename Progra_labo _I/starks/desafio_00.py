
from data_stark import lista_personajes


def analizar_set_datos():
    for heroe in lista_personajes:
        print("\n---- nombre: {0} - identidad: {1} - empresa: {2} -"
               " altura: {3} "
               "- peso: {4} - genero: {5} - color de ojos: {6} - "
               "color de pelo: {7} - fuerza: {8} - inteligencia: {9} ----\n"
            .format(heroe["nombre"], heroe["identidad"],
              heroe["empresa"], heroe["altura"], heroe["peso"],
              heroe["genero"], heroe["color_ojos"], heroe["color_pelo"],
                    heroe["fuerza"], heroe["inteligencia"]))


def imprimir_nombre_superheroe():
    for heroe in lista_personajes:
         print("\t Nombre: {0} \n".format(heroe["nombre"]))


def imprimir_nombre_altura():
       for heroe in lista_personajes:
         print("\t Nombre: {0} - Altura {1}\n"
               .format(heroe["nombre"], heroe["altura"]))


def calcular_mas_alto():

    indice_alto = 0

    for indice in range(len(lista_personajes)):
        if indice == 0 or float(lista_personajes[indice]["altura"]) > float(
                lista_personajes[indice_alto]["altura"]):
               indice_alto = indice
               
    print("\nEl superhéroe más alto es : {0} y la altura es : {1}\n"
          .format(lista_personajes[indice_alto]["nombre"],
                  lista_personajes[indice_alto]["altura"]))
    
def calcular_mas_bajo():

    indice_bajo = 0

    for indice in range(len(lista_personajes)):
        
        
        
        
        
        if indice == 0 or float(lista_personajes[indice]["altura"]) < float(
                lista_personajes[indice_bajo]["altura"]):
            indice_bajo = indice
            
            
            
            
            
    print("\nEl superhéroe más bajo es : {0} y la altura es : {1}\n"
          .format(lista_personajes[indice_bajo]["nombre"],
                  lista_personajes[indice_bajo]["altura"]))








def calcular_altura_promedio():

    acumulador_personajes = 0

    for personaje in lista_personajes:
        acumulador_personajes += float(personaje["altura"])

    print("\nEl promedio de altura es : {0}\n"
          .format(acumulador_personajes / len(lista_personajes)))


def informa_nombre_mas_alto_bajo():

    indice_altura_bajo = 0
    indice_altura_alto = 0

    for indice in range(len(lista_personajes)):
        if indice == 0 or float(lista_personajes[indice]["altura"]) > float(
            lista_personajes[indice_altura_alto]["altura"]):
               indice_altura_alto = indice
        if indice == 0 or float(lista_personajes[indice]["altura"]) < float(
            lista_personajes[indice_altura_bajo]["altura"]):
               indice_altura_bajo = indice

    print("\n El superhéroe más alto es : {0} y el superhéroe más bajo es : {1} \n"
          .format(lista_personajes[indice_altura_alto]["nombre"],
                  lista_personajes[indice_altura_bajo]["nombre"]))

def calular_peso():

    indice_peso_alto = 0
    indice_peso_bajo = 0

    for indice in range(len(lista_personajes)):
        if indice == 0 or float(lista_personajes[indice]["peso"]) > float(
                lista_personajes[indice_peso_alto]["peso"]):
               indice_peso_alto = indice
        if indice == 0 or float(lista_personajes[indice]["peso"]) < float(
                lista_personajes[indice_peso_bajo]["peso"]):
               indice_peso_bajo = indice
    print("\nEl superhéroe más pesado es : {0} y El superhéroe menos pesado es : {1} \n"
          .format(lista_personajes[indice_peso_alto]["nombre"],
                  lista_personajes[indice_peso_bajo]["nombre"]))
 
def mostrar_menu():
    print("A)Analizar detenidamente el set de datos")
    print("B)Recorrer la lista imprimiendo por consola el nombre de cada"
          " superhéroe")
    print("C)Recorrer la lista imprimiendo por consola nombre de cada"
          " superhéroe junto a la altura del mismo")
    print("D)Recorrer la lista y determinar cuál es el superhéroe más alto"
          " (MÁXIMO)")
    print("E)Recorrer la lista y determinar cuál es el superhéroe más bajo"
          " (MÍNIMO)")
    print("F)Recorrer la lista y determinar la altura promedio de los "
          "superhéroes (PROMEDIO)")
    print("G)Informar cual es el Nombre del superhéroe asociado a cada uno de "
          "\nlos indicadores anteriores (MÁXIMO, MÍNIMO)")
    print("H)Calcular e informar cual es el superhéroe más y menos pesado.")
    print("I) salir")
    
while True:
   
    mostrar_menu()
    opcion = input("Ingrese una opcion: ")
    match opcion:
        case "A":
            analizar_set_datos()
        case "B":
            imprimir_nombre_superheroe()
        case "C":
            imprimir_nombre_altura()
        case "D":
            calcular_mas_alto()
        case "E":
            calcular_mas_bajo()
        case "F":
            calcular_altura_promedio()
        case "G":
            informa_nombre_mas_alto_bajo()
        case "H":
            calular_peso()
        case "I":
            break
        case _:
            print('Error no disponible.')

