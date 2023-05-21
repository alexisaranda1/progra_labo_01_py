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

def validacion(opcion : str, expresion : str):
    """
    La función toma una cadena y una expresión regular y devuelve la cadena original si coincide con la
    expresión regular; de lo contrario, devuelve "-1".
    
    @param opcion una variable de cadena que representa la opción de entrada del usuario
    @param expresion El parámetro "expresión" es un patrón de expresión regular que se utiliza para
    validar el parámetro "opcion". Es una cadena que contiene un conjunto de reglas que definen lo que
    se considera una entrada válida para el parámetro "opcion". El patrón de expresión regular se usa
    para hacer coincidir la cadena de entrada con
    
    @return la opción validada como una cadena. Si la opción no coincide con la expresión regular
    proporcionada en el parámetro "expresión", devolverá "-1".
    """
 
    opcion_validado = "-1"
  
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


def ordenar_por_clave(lista: list[dict], clave: str, flag_orden: bool):
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
    return lista_nueva
                
def stark_marvel_app (lista_personajes: list[dict])-> None:
    stark_normalizar_datos(lista_personajes)

    while True:
        mensaje_error = "Error, incorrecto!"
        imprimir_menu_Desafio()
        opcion = input("Ingrese una opcion: ")
        opcion = validacion(opcion , r'^[1-7]{1}$')
        int_opcion = int(opcion)

        match int_opcion:
            case 1:

                numero_str = input("\n\n\n\nIngrese la cantidad de heroes a imprimir: ")
                numero_str = validacion(numero_str , r'^[0-9]{1,2}$')
                numero_entero = int(numero_str)

                if numero_entero <= len(lista_personajes) and numero_entero < 0:
                    for i in range(numero_entero):
                        print("Nombre : {0}".format(lista_personajes[i]["nombre"]))
                else: 
                   imprimir_dato(mensaje_error) 
            case 2:
                forma_ordenar = input("\n\n\n\nIngrese (asc) para ordenar de forma acendente o (desc) para ordenar de forma desendente: ")
                forma_ordenar = validacion(forma_ordenar , r'^(asc|desc)$')

                if forma_ordenar == "asc":
                    lista_ordenada = ordenar_por_clave(lista_personajes,"altura", False)
                    for personaje in lista_ordenada:
                        nombre = personaje["nombre"]
                        altura = personaje["altura"]
                        mesaje = "Nombre : {0}, altura : {1}".format(nombre, altura)
                        imprimir_dato(mesaje)
                elif forma_ordenar == "desc":
                    lista_ordenada = ordenar_por_clave(lista_personajes,"altura", True)
                    for personaje in lista_ordenada:
                        nombre = personaje["nombre"]
                        altura = personaje["altura"]
                        mesaje = "Nombre : {0}, altura : {1}".format(nombre, altura)
                        imprimir_dato(mesaje)

                else :
                    imprimir_dato(mensaje_error) 
                pass
            case 3:
                forma_ordenar = input("\n\n\n\nIngrese (asc) para ordenar de forma acendente o (desc) para ordenar de forma desendente: ")
                forma_ordenar = validacion(forma_ordenar , r'^(asc|desc)$')
                if forma_ordenar == "asc":
                    lista_ordenada = ordenar_por_clave(lista_personajes,"fuerza", False)
                    for personaje in lista_ordenada:
                        nombre = personaje["nombre"]
                        fuerza = personaje["fuerza"]
                        mesaje = "Nombre : {0}, fuerza : {1}".format(nombre, fuerza)
                        imprimir_dato(mesaje)
                elif forma_ordenar == "desc":
                    lista_ordenada = ordenar_por_clave(lista_personajes,"fuerza", True)
                    for personaje in lista_ordenada:
                        nombre = personaje["nombre"]
                        fuerza = personaje["fuerza"]
                        mesaje = "Nombre : {0}, fuerza : {1}".format(nombre, fuerza)
                        imprimir_dato(mesaje)

                else :
                    imprimir_dato(mensaje_error) 
                pass
            case 4:
                pass
            case 5:

                intelengencia_buscar = input("\n\n\n\nIngrese el tipo de inteligencia [good, average, high]: ")
                intelengencia_buscar = validacion(intelengencia_buscar , r'^(good|average|high)$')
                if intelengencia_buscar != "-1" :
                    for personaje in lista_personajes:  
                        if intelengencia_buscar == personaje["inteligencia"]:               
                            nombre = personaje["nombre"]
                            mesaje = "Nombre : {0}, inteligencia : {1}".format(nombre, intelengencia_buscar)
                            imprimir_dato(mesaje)
                else :
                    imprimir_dato(mensaje_error)


                    
            case 6:
                pass
            case 7:
                print("Salio del progrma!")
                break
            case _:
                 imprimir_dato(mensaje_error) 

        clear_console()           




ruta = r"starks\data_stark.json"
lista_personajes = leer_archivo(ruta)
stark_marvel_app(lista_personajes)