import json
import re

import os

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

def imprimir_dato(cadena_caracteres: str):
    """
    La función "imprimir_dato" comprueba si la entrada es una cadena y la imprime, de lo contrario,
    imprime un mensaje diciendo que no es una cadena.
    
    @param cadena_caracteres una variable de tipo cadena que representa una secuencia de caracteres.
    """
    if type(cadena_caracteres) == str:
        print(cadena_caracteres)
    else:
        print("No es una cadena de texto")

def imprimir_menu_Desafio():
    """
    Esta función imprime un menú con diferentes opciones.

    """
    menu = '''\n\t------------------- Menu---------------------------------------\n

    1) Listar por pantalla los juegos cuyo género no contenga la palabra “pelea”.
    2) Calcular y mostrar la cantidad de juegos de una década determinada, la misma será 
    ingresada por el usuario por pantalla.  
    3) Listar los juegos ordenados por Empresa. Preguntar al usuario si lo quiere ordenar de    
    manera ascendente (‘asc’) o descendente („desc‟).
    4) Buscar juegos por modo [multijugador, cooperativo] y listar en consola los que cumplan 
    dicha búsqueda. (Usando RegEx).
    5) Exportar a CSV la lista de juegos según opción 1 o 3.
    6) Salir.

    '''
    imprimir_dato(menu)



def validar_opcion_expresion(expresion: str, ingreso_teclado: str, busqueda = False) -> str:
    """
    Valida una opción utilizando una expresión regular y devuelve la opción si coincide;
    de lo contrario, devuelve "-1".
    
    Parametros: 
        -expresion: La expresión regular utilizada para validar la opción.
        -opcion: La opción de entrada del usuario.
        -usar_search: Indica si se debe utilizar el método `search` (True) o `match` (False) para
          la validación.

    Retorno: 
        La opción validada como una cadena. Si la opción no coincide con la expresión
        regular utilizando el método especificado, se devuelve "-1".
    """
    opcion_validada = "-1"

    if busqueda:
        if re.search(expresion, ingreso_teclado):
            opcion_validada = ingreso_teclado
    else:
        if re.match(expresion, ingreso_teclado):
            opcion_validada = ingreso_teclado

    return opcion_validada

def stark_normalizar_datos(lista_heroes: list[dict]) -> None:
    """
    Normaliza los datos en una lista de diccionarios convirtiendo
    ciertos valores de cadena en números enteros o flotantes.
    Parametro:
        -lista_heroes: list[dict]: Una lista de diccionarios que representan héroes y sus atributos
    Retorno : 
        -None: la funcion no retorna ningun valor.
    """
    if lista_heroes:
        # Recorro cada diccionario de heroe de la lista
        for heroe in lista_heroes:
            key_list = list(heroe.keys())
            # Recorro las claves que me interesan castear
            for key in key_list:

                if type(heroe[key]) is str:
                    
                    if not heroe[key]:
                        heroe[key]= 'No tiene'
                        print(heroe)
                    else:
                        valor_reemplazado: str = heroe[key].replace(
                            '.', '')  # reemplaza un "." por un ""
                        if type(heroe[key]) is str and valor_reemplazado.isnumeric():
                            if '.' in heroe[key] and heroe[key].count('.') == 1:
                                # verificar si el valor de la clave key
                                # contiene exactamente un punto en su interior
                                heroe[key] = float(heroe[key])
                            else:
                                heroe[key] = int(heroe[key])
                                # print(f'El dato {key} fue modificada para el heroe: {heroe["nombre"]}')
    else:
        print('Error La lista esta vacía.')

def leer_archivo(ruta: str)-> list:
    """
    La función lee un archivo JSON de una ruta determinada y devuelve una lista de héroes del archivo.
    
    @param ruta El parámetro "ruta" es una cadena que representa la ruta del archivo JSON que debe
    leerse.
    
    @return una lista de héroes leída de un archivo JSON ubicado en la ruta especificada.
    """

    with open(ruta, 'r') as archivo:
        contenido = json.load(archivo)
        lista_heroes = contenido['juegos']
    return lista_heroes

def guardar_archivo(nombre_archivo:str, contenido)-> bool:
    """
    Esta función guarda el contenido dado en un archivo con el nombre especificado 
    y devuelve un booleano
    indicando si la operación fue exitosa.
    :param nombre_archivo: Una cadena que representa el nombre del archivo a crear o sobrescribir
    :param contenido: El contenido que se escribirá en el archivo. Puede ser una cadena o cualquier 
    otro dato.
    tipo que se puede convertir en una cadena
    :return: un valor booleano que indica si el archivo se creó correctamente o no. cierto es
    se devuelve si el archivo se creó correctamente y se devuelve False si hubo un error al crearlo.
    el archivo.
    """

    with open(nombre_archivo, 'w+') as archivo:
        resultado = None
        resultado = archivo.write(contenido)
    if resultado:
        print("Se creó el archivo: {0}".format(nombre_archivo))
        return True

    print("Error al crear el archivo: {0}".format(nombre_archivo))
    return False

import re

import re


def filtrar_por_palabra(lista_juegos: list[dict]) -> list:
    """
    Esta función filtra una lista de diccionarios que contienen información de videojuegos eliminando
    cualquier juego con la palabra "pelea" (lucha) en la clave "genero" (género).
    
    @param lista_juegos una lista de diccionarios que representan videojuegos, donde cada diccionario
    contiene información sobre un solo juego, como su nombre, género, fecha de lanzamiento, etc.
    
    @return una lista filtrada de diccionarios que contienen juegos que no tienen la palabra "pelea"
    en su clave "genero" (género).
    """
    lista_filtrada = []

    if lista_juegos:
        for juego in lista_juegos:
            if not re.search(r'pelea', juego["genero"], re.IGNORECASE):
                print("Nombre : {0} | Genero: {1}".format(juego["nombre"], juego['genero']))
                lista_filtrada.append(juego)

    return lista_filtrada

def filtra_por_decada(lista_juegos: list[dict])-> list:

    lista_filtrada = []

    if lista_juegos:
        opcion = input("Ingrese la decada: ")
        opcion = validar_opcion_expresion(r'^([19|20]{2}[0-9]{1,2})$ ', opcion)
        print(opcion)
    return lista_filtrada

def juegos_app (lista_juegos: list[dict])-> None:

    #stark_normalizar_datos(lista_juegos) 

    lista_filtrada = []

    while True:


        mensaje_error = "Error, incorrecto!"
        imprimir_menu_Desafio()
        opcion = input("Ingrese una opcion: ")
        opcion = validar_opcion_expresion(r'^[1-6]{1}$', opcion )
        int_opcion = int(opcion)

        match int_opcion:
            case 1:
                lista_filtrada = filtrar_por_palabra(lista_juegos)
            case 2: 
                lista_filtrada = filtra_por_decada(lista_juegos)
            case 3:
                pass
            case 4:
               pass
            case 5:
                if lista_filtrada:
                    pass
                pass
            case 6:
                print("Salio del progrma!")
                break  
            case _:
                 imprimir_dato(mensaje_error) 

        clear_console()     

ruta = r"starks\data_juegos.json"
lista_juegos = leer_archivo(ruta)
juegos_app(lista_juegos)

