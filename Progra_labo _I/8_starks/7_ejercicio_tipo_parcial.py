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
    rango_a = len(lista) -1 
    flag_swap = True

    while flag_swap:
        flag_swap = False

        for indice_A in range(rango_a):  
            if (flag_orden == False and lista_nueva[indice_A][clave] < lista_nueva[indice_A+1][clave]) \
                    or (flag_orden == True and lista_nueva[indice_A][clave] > lista_nueva[indice_A+1][clave]):
                lista_nueva[indice_A], lista_nueva[indice_A+1] = lista_nueva[indice_A+1], lista_nueva[indice_A]

                flag_swap = True
    return lista_nueva

def calcular_promedio_lista_diccionarios(lista: list[dict],clave:str)->float:
    """
    Esta función calcula el valor promedio de una clave específica en una lista de diccionarios.
    
    @param lista una lista de diccionarios
    @param clave El parámetro "clave" es una cadena que representa la clave o atributo de los
    diccionarios de la lista que se utilizará para calcular el promedio.
    
    @return un valor flotante, que es el promedio de los valores asociados con la clave especificada en
    los diccionarios de la lista de entrada. Si la lista está vacía o no hay valores válidos para la
    clave especificada, la función devuelve 0.
    """
    acumulador = 0
    contador = 0
    resultado = 0
    if len(lista) == 0:
        return 0
    for diccionario in lista:
        if clave in diccionario:
            if type(diccionario[clave]) == int or type(diccionario[clave]) == float:
                acumulador += diccionario[clave]
                contador += 1
    if contador > 0:
        resultado = acumulador / contador
    return resultado

def listar_primeros_n_heroes(lista_heroes: list[dict])-> list:
    """
    Esta función toma una lista de diccionarios que contienen información sobre héroes y solicita al
    usuario que ingrese un número, luego imprime los nombres de los primeros n héroes en la lista.

    Parametro: 
        -lista_heroes Una lista de diccionarios que representan héroes.
    
    Retorno:  
        -la lista original de héroes (lista_heroes) después de modificar potencialmente una copia de
        la misma (lista_aux). Sin embargo, la función en realidad no modifica la lista de ninguna manera,
        por lo que lista_aux es idéntica a lista_heroes.
    """
    lista_aux = []
    if lista_heroes:
        
        numero_str = input("\n\n\n\nIngrese la cantidad de heroes a imprimir: ")
        numero_str = validar_opcion_expresion(r'^[0-9]{1,2}$', numero_str)
        numero_entero = int(numero_str)
        
        if numero_entero <= len(lista_heroes) and numero_entero > 0:
            
            for heroe in lista_heroes[:numero_entero]: 
                print(heroe)
                lista_aux.append(heroe)  
        else: 
            print("Error!")

    return lista_aux

def ordena_listar_clave(lista_heores : list[dict], clave: str )->list:
    """
    Esta función ordena una lista de diccionarios que contienen información de héroes en función de una
    clave específica en orden ascendente o descendente.
    
    Parametros: 
        lista_heores El parámetro "lista_heores" es una lista de diccionarios que representan héroes.
        clave El parámetro "clave" es una cadena que representa la clave o atributo del diccionario
        en la lista de héroes que se utilizará para ordenar la lista.
    
    Retorno:    
        La función puede devolver un número entero (-1) o una lista de diccionarios
        (lista_ordenada).
    """
    lista_ordenada = []
    if lista_heores:
        forma_ordenar = input("\n\n\n\nIngrese (asc) para ordenar de forma acendente o (desc) para ordenar de forma desendente: ")
        forma_ordenar = validar_opcion_expresion(r'^(asc|desc)$', forma_ordenar, True)
        print(forma_ordenar)
        
        if forma_ordenar == "asc":
            forma_ordenar = True
        elif forma_ordenar == "desc":
            forma_ordenar = False
        else: 
            return lista_ordenada
        
        orden = bool(forma_ordenar)

        lista_ordenada = ordenar_por_clave(lista_personajes, clave , orden ) 
        for personaje in lista_ordenada:
            nombre = personaje["nombre"]
            valor = personaje[clave]
            mesaje = "Nombre : {0}, {1} : {2}".format(nombre, clave ,valor)
            imprimir_dato(mesaje)
            
    return lista_ordenada


def filtrar_por_promedio(lista_original: list, clave: str)-> list:

    """
    Esta función filtra una lista de diccionarios en función de si el valor de una clave específica es
    mayor o menor que el valor promedio de esa clave en la lista y permite al usuario elegir si ordenar
    la lista filtrada en orden ascendente o descendente.
    
    Parametros: 
        -lista_original Una lista de diccionarios que contienen información sobre héroes.
        -clave El parámetro "clave" es una cadena que representa la clave o atributo de los
        diccionarios en el parámetro "lista_original" que se usará para calcular el promedio y filtrar la
        lista.
    
    Retorno: 
        ya sea una lista de diccionarios filtrados en función de una clave dada y una dirección de
        filtro ingresada por el usuario (ascendente o descendente), o -1 si la lista original está vacía.

    """
    lista_filtrada = []
    if lista_original:
      
        forma_filtro= input("\n\nIngrese ‘menor’ o ‘mayor’ para imprimir los que correspondan: ")
        forma_filtro_validado = validar_opcion_expresion(r'^(mayor|menor)$', forma_filtro, True)

        lista = lista_original[:]
        lista_filtrada = []
        promedio = calcular_promedio_lista_diccionarios(lista, clave)
        print("El promedio : {0}".format(promedio))
        for heroe in lista:
            if forma_filtro_validado == "mayor":
                if heroe[clave] > promedio:
                    print("Nombre: {0} |{1}: {2} ".format(heroe["nombre"],clave ,heroe[clave]))
                    lista_filtrada.append(heroe)
            elif forma_filtro_validado == "menor":
                if heroe[clave] < promedio:
                    print("Nombre: {0} |{1}: {2} ".format(heroe["nombre"],clave ,heroe[clave]))
                    lista_filtrada.append(heroe)

    return lista_filtrada
    

def filtrar_por_inteligencia(lista_heores: list[dict])-> None:
    """
    Esta función filtra una lista de héroes por su nivel de inteligencia según la entrada del usuario.
    
    Parametro:
        -lista_heores Una lista de diccionarios que representan héroes, donde cada diccionario
        contiene información sobre un héroe, como su nombre, nivel de inteligencia, etc.
    
    Retorno:
        -ya sea una lista de diccionarios que contienen solo los héroes con el nivel de inteligencia
        especificado, o -1 si la lista de entrada está vacía o la entrada del usuario para el nivel de
        inteligencia no es válida.
    """

    if lista_heores:
        lista_aux = lista_heores[:]
        intelengencia_buscar = input("\n\n\n\nIngrese el tipo de inteligencia [good, average, high]: ")
        intelengencia_buscar = validar_opcion_expresion('^(good|average|high)$', \
                                                        intelengencia_buscar, True)
        if intelengencia_buscar != "-1" :
            for personaje in lista_aux:  
                if intelengencia_buscar == personaje["inteligencia"]:               
                    nombre = personaje["nombre"]
                    mesaje = "Nombre : {0}, inteligencia : {1}".format(nombre, intelengencia_buscar)
                    imprimir_dato(mesaje)
        else:
            print("Error!")


def generar_texto(lista_diccionarios : list[dict])->str:
    """
    Esta función toma una lista de diccionarios y devuelve una cadena con las claves como primera línea
    y los valores de cada diccionario como líneas subsiguientes separadas por comas.

    Parametros:
        lista_diccionarios (list[dict]): Una lista de diccionarios, donde cada diccionario representa una fila de
            datos y las claves representan los nombres de las columnas.

    Returno:
        str: Una cadena que contiene las claves de los diccionarios en la lista de entrada separadas por
            comas en la primera línea, y los valores de cada diccionario en la lista de entrada separados por
            comas y nuevas líneas en las líneas siguientes.
    """

    texto_generado = ""

    if lista_diccionarios:
        primer_diccionario = lista_diccionarios[0]
        claves = []
        for clave in primer_diccionario.keys():
            claves.append(clave)

        texto_claves = ','.join(claves) 
        texto_valores = ''
        for diccionario in lista_diccionarios:
            valores = []
            for valor in diccionario.values():
                valores.append(str(valor))

            texto_valores += ','.join(valores) + '\n'  

        texto_generado = texto_claves + '\n' + texto_valores 

    return texto_generado

    
def guarda_opcion(nombre_archivo, lista_heores: list[dict])-> bool:

    """
    Esta función toma un nombre de archivo y una lista de diccionarios, genera texto de la lista y lo
    guarda en el archivo.
    
    @param nombre_archivo El nombre del archivo donde se guardará el contenido.
    @param lista_heores El parámetro "lista_heores" es una lista de diccionarios que contienen
    información sobre héroes.
    
    @return un valor booleano. Si el archivo se guarda correctamente, devuelve True. De lo contrario,
    devuelve False.
    """

    contenido = ""
    contenido = generar_texto(lista_heores)

    return guardar_archivo(nombre_archivo, contenido)


def stark_marvel_app (lista_personajes: list[dict])-> None:
    stark_normalizar_datos(lista_personajes)
    lista_filtrada = []
    nombre_archivo = ""

    while True:
        mensaje_error = "Error, incorrecto!"
        imprimir_menu_Desafio()
        opcion = input("Ingrese una opcion: ")
        opcion = validar_opcion_expresion(r'^[1-7]{1}$', opcion )
        int_opcion = int(opcion)

        match int_opcion:

            case 1:
                lista_filtrada = listar_primeros_n_heroes(lista_personajes)
                nombre_archivo = r"starks\paracial_lista_n_heores.csv"
            case 2: 
                lista_filtrada = ordena_listar_clave(lista_personajes, "altura")
                nombre_archivo = r"starks\parcial_lista_ordenada_altura.csv"
            case 3:
                lista_filtrada = ordena_listar_clave(lista_personajes, "fuerza")
                nombre_archivo = r"starks\paracial_lista_orenada_fuerza.csv"
            case 4:  
                lista_filtrada = filtrar_por_promedio(lista_personajes, "fuerza")
                nombre_archivo = r"starks\parcial_lista_filtrada_por_promedio.csv"
            case 5:
                lista_filtrada_inteligencia = filtrar_por_inteligencia(lista_personajes)
            case 6:
                if lista_filtrada:
                    guarda_opcion(nombre_archivo, lista_filtrada) 
                    lista_filtrada = None
                else: 
                    print("No entro a un case, no puede guradar el archivo!")         
            case 7:
                print("Salio del progrma!")
                break
            case _:
                 imprimir_dato(mensaje_error) 

        clear_console()           

ruta = r"starks\data_stark.json"
lista_personajes = leer_archivo(ruta)
stark_marvel_app(lista_personajes)