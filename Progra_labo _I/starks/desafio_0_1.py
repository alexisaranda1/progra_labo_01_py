
from data_stark import lista_personajes


'''
 Agregar al código elaborado para cumplir el desafío #01 los siguientes puntos,
 utilizando un menú que permita acceder a cada uno de los puntos por separado.

 '''

def muestra_menu():
    print("A)Recorrer la lista imprimiendo por consola el nombre de cada"
          "superhéroe de género M")
    print("B)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F")
    print("C)Recorrer la lista y determinar cuál es el superhéroe más alto de género M ")
    print("D)Recorrer la lista y determinar cuál es el superhéroe más alto de género F ")
    print("E)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M ")
    print("F)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F ")
    print("G)Recorrer la lista y determinar la altura promedio de los "
          "superhéroes de género M")
    print("H)Recorrer la lista y determinar la altura promedio de los  "
          "superhéroes de género F")
    print("I)Informar cual es el Nombre del superhéroe asociado a cada uno de"
          " los indicadores anteriores (ítems C a F)")
    print("J)Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("K)Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("L)Determinar cuántos superhéroes tienen cada tipo de inteligencia "
          " (En caso de no tener, Inicializarlo con ‘No Tiene’). ")
    print("M)Listar todos los superhéroes agrupados por color de ojos.")
    print("N)Listar todos los superhéroes agrupados por color de pelo.")
    print("O)Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("P) para volver al menu principal.")


def recorre_imprime_nombre_segundo_genero(lista_heroes: list, genero: str) -> None:

    for heroe in lista_heroes:
        if heroe["genero"] == genero:
            print(heroe["nombre"])


def heroe_segun_altura_genero(lista_heroes: list, genero: str, min_max: str, falg =0) -> None:
    heroe_aux = {}
    
        
    for heroe in lista_heroes:
        
        if not heroe_aux and heroe['genero'] == genero:
            heroe_aux = heroe
        if (heroe_aux and heroe['genero'] == genero):
            if ((min_max == 'Bajo' and float(heroe_aux['altura']) > float(
                heroe['altura']))
                or
                (min_max == 'Alto' and float(heroe_aux['altura']) < float(
                    heroe['altura']))):
                heroe_aux = heroe
    if falg == 0:            
        imprime_un_heroe(heroe_aux)
    else:
        print("\n\tNombre: {0}\n".format(heroe_aux['nombre']))


def calcular_promedio_altura_segun_genero(lista_heroes: list, genero: str) -> None:
    acumulador_personajes = 0
    contador = 0

    for heroe in lista_heroes:
        if genero == 'M' and heroe['genero'] == genero or genero == 'F' and heroe['genero'] == genero:
            acumulador_personajes += float(heroe["altura"])
            contador += 1

    print("\nEl promedio de altura del genero: {0} es {1:.2f}\n"
          .format(genero, acumulador_personajes / contador))

def imprime_un_heroe(heroe):
    print(f"\n\tNombre: {heroe['nombre']} - Altura: {heroe['altura']} mts.\n")

def contar_color_ojos(lista_heroes):
    color_ojos_dict = {}
    for heroe in lista_heroes:
        color_ojos = heroe['color_ojos']
        if color_ojos in color_ojos_dict:
            color_ojos_dict[color_ojos] += 1
        else:
            color_ojos_dict[color_ojos] = 1
    return color_ojos_dict

def contar_color_pelo(lista_heroes):
    color_pelo_dict = {}
    for heroe in lista_heroes:
        color_pelo = heroe['color_pelo']
        if color_pelo in color_pelo_dict:
            color_pelo_dict[color_pelo] += 1
        else:
            color_pelo_dict[color_pelo] = 1
    return color_pelo_dict

def contar_inteligencia(lista_heroes):
    dic_inteligencia = {}
    for heroe in lista_heroes:
        if 'inteligencia' in heroe and heroe['inteligencia'] != '':
            inteligencia = heroe['inteligencia']
        else:
            inteligencia = 'No Tiene'
        if inteligencia in dic_inteligencia:
            dic_inteligencia[inteligencia] += 1
        else:
            dic_inteligencia[inteligencia] = 1
            
    for clave in dic_inteligencia.keys():
        valor = dic_inteligencia[clave]   
        print("\t: Inteligencia {0} , Cantidad: {1} ".format(clave, valor))

def mostar_cantidad (cantida_color):
    
    for clave in cantida_color.keys():
        valor = cantida_color[clave]   
        print("\tcolor: {0} , Cantidad: {1} ".format(clave, valor))

def agrupar_por_atributo(lista_heroes, key):
    
    '''
    agrupa una lista de diccionarios de héroes según un atributo especificado.
    Parametros:
    lista_heroes -- lista de diccionarios de héroes
    key -- puede tomar la clave que necesite agrupar
    Retorna :
     diccionario -- con las listas  
    de diccionarios agrupadas según el valor del atributo especificado.
    '''

    if not lista_heroes:
        
        return {}
    if key not in lista_heroes[0]:
        return {}
    diccionario = {}
    for heroe in lista_heroes:
        if key in heroe and heroe[key] != "":
            valor_atributo = heroe[key]
            
        else:
            valor_atributo = 'No Tiene'
            
        if valor_atributo in diccionario:
            diccionario[valor_atributo].append(heroe)
        else:
            diccionario[valor_atributo] = [heroe]
            
    return diccionario

def imprimir_diccionario(diccionario):
    for clave in diccionario:
        print(clave + ":")
        for elemento in diccionario[clave]:
            print("\t- " + elemento["nombre"])
   

def listar_por_color_ojos(heroes):
    diccionario_ojos = agrupar_por_atributo(heroes, 'color_ojos')
    imprimir_diccionario(diccionario_ojos)
    
def listar_por_color_pelo(heroes):
    diccionario_pelo = agrupar_por_atributo(heroes, 'color_pelo')
    imprimir_diccionario(diccionario_pelo)
    

def listar_por_tipo_inteligencia(heroes):  
    diccionario_inteligencia = agrupar_por_atributo(heroes, 'inteligencia')
    imprimir_diccionario(diccionario_inteligencia)

def desafio_01(lista_personajes):

    while True:
        muestra_menu()
        opcion = input("Ingrese una opcion: ")
        match opcion:
            case "A":
                recorre_imprime_nombre_segundo_genero(lista_personajes, "M")
            case "B":
                recorre_imprime_nombre_segundo_genero(lista_personajes, "F")
            case "C":
                heroe_segun_altura_genero(lista_personajes, "M", "Alto")
            case "D":
                heroe_segun_altura_genero(lista_personajes, "F", "Alto")
            case "E":
                heroe_segun_altura_genero(lista_personajes, "M", "Bajo")
            case "F":
                heroe_segun_altura_genero(lista_personajes, "F", "Bajo")
            case "G":
                calcular_promedio_altura_segun_genero(lista_personajes, 'M')
            case "H":
                calcular_promedio_altura_segun_genero(lista_personajes, 'F')
            case "I":
                heroe_segun_altura_genero(lista_personajes, "M", "Alto", 1)
                heroe_segun_altura_genero(lista_personajes, "F", "Bajo", 1)
            
            case "J":
                dict_cantidad_color_ojos = contar_color_ojos(lista_personajes)
                mostar_cantidad(dict_cantidad_color_ojos)
    
            case "K":
                mostar_cantidad(contar_color_pelo(lista_personajes))
            case "L":
                contar_inteligencia(lista_personajes)
            case "M":
                listar_por_color_ojos(lista_personajes)

            case "N":
                listar_por_color_pelo(lista_personajes)
            case "O":
                listar_por_tipo_inteligencia(lista_personajes)
            case "P":
                break
            case _:
                print('Error no disponible.')





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
    print("I)ir al menu stark 01")
    print("J) salir")
    
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
            desafio_01(lista_personajes)
        case "J":
            break
        case _:
            print('Error no disponible.')
###
###
###
###
##
##
##
##
##
###
###
###
###
####
