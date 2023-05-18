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
    1) Listar los primeros N héroes. El valor de N será ingresado por 
    el usuario  (Validar que no supere max. de lista)

    2) Ordenar y Listar héroes por altura. Preguntar al usuario si lo
      quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)

    3) Ordenar y Listar héroes por fuerza. Preguntar al usuario
      si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)

    4) Calcular promedio de cualquier key numérica, filtrar los que cumplan 
    con la condición de superar o no el promedio (preguntar al usuario la 
    condición: ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que 
    cumplan con ser mayores o menores según corresponda.

    5)  Buscar héroes por inteligencia [good, average, high] y
      listar en consola los que cumplan dicha búsqueda. (Usando RegEx)

    6)  Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]


    '''
    imprimir_dato(menu)

def stark_menu_principal_desafio(opcion : str, expresion : str):
    """
    Esta función muestra un menú y solicita al usuario que ingrese una opción, devolviendo la opción si
    coincide con un patrón determinado o -1 de lo contrario.
    
    @return Si la entrada del usuario coincide con el patrón de expresión regular '[A-OZ]{1}', la
    función devolverá la cadena de entrada en mayúsculas. De lo contrario, devolverá -1.
    """
    opcion_validado = "-1"
    imprimir_menu_Desafio()

    #if re.match('^[1-7]{1}$', opcion):
    if re.match(expresion, opcion):   
        opcion_validado = opcion

    return opcion_validado
def stark_normalizar_datos(lista_heroes: list[dict]) -> None:
    '''Recorrer la lista y convertir al tipo de dato correcto las keys (solo con las keys que 
    representan datos numéricos)
    Validar primero que el tipo de dato no sea del tipo al cual será casteado. Por ejemplo si 
    una key
    debería ser entero (ejemplo edad) verificar antes que no se encuentre ya en ese tipo de dato.
    Si al menos un dato fue modificado, la función deberá imprimir como mensaje ‘Datos normalizados’,
    caso contrario no imprimirá nada.
    Validar que la lista de héroes no esté vacía para realizar sus acciones,
    caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”

    '''
    if lista_heroes:
        # Recorro cada diccionario de heroe de la lista
        for heroe in lista_heroes:
            key_list = list(heroe.keys())
            # Recorro las claves que me interesan castear
            for key in key_list:
                if type(heroe[key]) is str:
                    valor_reemplazado: str = heroe[key].replace('.', '') # reemplaza un "." por un ""
                    if   type(heroe[key]) is str and valor_reemplazado.isnumeric():
                        if '.' in heroe[key] and heroe[key].count('.') == 1:
                        
                            heroe[key] = float(heroe[key])
                        else:
                            heroe[key] = int(heroe[key])
                           

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
        lista_heroes = contenido['heroes']
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


def ordenar_por_clave(lista, flag_orden, clave):
    """
    Ordena una lista de diccionarios en base a una clave específica.

    Args:
        lista (list): La lista de diccionarios a ordenar.
        flag_orden (bool): Indica el tipo de ordenamiento. False para orden ascendente, True para orden descendente.
        clave (str): La clave en los diccionarios por la cual se realizará el ordenamiento.

    Returns:
        list: Una nueva lista de diccionarios ordenada en base a la clave especificada.
    """
    lista_nueva = lista[:]
    rango_a = len(lista) - 1
    flag_swap = True

    while flag_swap:
        flag_swap = False

        for indice_A in range(rango_a):
            if (flag_orden == False and lista_nueva[indice_A][clave] < lista_nueva[indice_A+1][clave]) \
                    or (flag_orden == True and lista_nueva[indice_A][clave] > lista_nueva[indice_A+1][clave]):
                
                lista_nueva[indice_A], lista_nueva[indice_A+1] = lista_nueva[indice_A+1], lista_nueva[indice_A]
                flag_swap = True

                
def stark_marvel_app (lista_personajes: list[dict])-> None:
    stark_normalizar_datos(lista_personajes)

    while True:
        opcion = input("Ingrese una opcion: ")
        opcion = stark_menu_principal_desafio(opcion , r'^[1-7]{1}$')

        match opcion:
            case 1:
                
                #  re.match('[0-9]{1,2}', N:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                break
            case _:
                print("opcion incorrecta!")

        clear_console()           




ruta = r"starks\data_stark.json"
lista_personajes = leer_archivo(ruta)