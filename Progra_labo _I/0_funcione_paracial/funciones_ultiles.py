import re
import json


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

# 1.1


def imprimir_menu_Desafio_5() -> None:
    """
    Esta función imprime un menú con diferentes opciones para un desafío relacionado con los
    superhéroes.

    Retorno : 
        -None: la funcion no retorna ningun valor.
    """
    menu = '''\n\t------------------- Menu---------------------------------------\n
    A)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M.
    B)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F.
    C)Recorrer la lista y determinar cuál es el superhéroe más alto de género M. 
    D)Recorrer la lista y determinar cuál es el superhéroe más alto de género F.
    E)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M.
    F)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F.
    G)Recorrer la lista y determinar la altura promedio de los  superhéroes de género M.
    H)Recorrer la lista y determinar la altura promedio de los  superhéroes de género F.
    I)Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F).
    J)Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    K)Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    L)Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
    M)Listar todos los superhéroes agrupados por color de ojos.
    N)Listar todos los superhéroes agrupados por color de pelo.
    O)Listar todos los superhéroes agrupados por tipo de inteligencia.
    Z) para salir.
    '''
    imprimir_dato(menu)

# 1.2


def stark_menu_principal_desafio_5():
    """
    Esta función muestra un menú y solicita al usuario que ingrese una opción, devolviendo la opción si
    coincide con un patrón determinado o -1 de lo contrario.

    :retorno: ya sea la entrada del usuario (si coincide con el patrón de expresión regular) o -1 si la
    entrada no coincide con el patrón.
    """

    imprimir_menu_Desafio_5()
    opcion = input("Ingrese una opcion: ").upper()
    if re.match('[A-OZ]{1}', opcion):
        return opcion
    return -1

 # 1.2


def imprimir_dato(cadena_caracteres: str) -> None:
    """
    La función "imprimir_dato" comprueba si la entrada es una cadena y la imprime, de lo contrario
    imprime "No es una cadena de texto".

    Parametro:
      cadena_caracteres: de tipo string (str) que representa una
    secuencia de caracteres. 

     Retorno : 
        -None: la funcion no retorna ningun valor.
    """

    if type(cadena_caracteres) == str:
        print(cadena_caracteres)
    else:
        print("No es una cadena de texto")

# 1.4


def leer_archivo(ruta: str) -> list:
    """
    Esta función lee un archivo JSON de una ruta determinada y devuelve una lista de héroes.

    Parametro 
        -ruta:  es una cadena que representa la ruta del archivo JSON que contiene
        los datos a leer

    :return: una lista de héroes leída de un archivo JSON ubicado en la ruta especificada.

    """

    with open(ruta, 'r') as archivo:
        contenido = json.load(archivo)
        lista_heroes = contenido['heroes']
    return lista_heroes

# #1.5


def guardar_archivo(nombre_archivo: str, contenido: str) -> bool:
    """
    Esta función guarda el contenido de una cadena en un archivo con el nombre de archivo dado y
    devuelve un valor booleano que indica si la operación fue exitosa o no.

    Parametros: 
        -nombre_archivo: Una cadena que representa el nombre del archivo que se va a crear o
        sobrescribir

        -contenido: El contenido que se escribirá en el archivo. Debería ser una cadena

    :retorno: 
        -un valor booleano, ya sea True o False, según si el archivo se creó correctamente o no.
    """

    with open(nombre_archivo, 'w+') as archivo:
        resultado = None # 
        resultado = archivo.write(contenido)
    if resultado:
        print("Se creó el archivo: {0}".format(nombre_archivo))
        return True

    print("Error al crear el archivo: {0}".format(nombre_archivo))
    return False
# 1.6


def capitalizar_palabras(texto_capitalizar: str) -> str:
    """
    La función escribe en mayúsculas cada palabra en una cadena dada y devuelve la cadena en mayúsculas.

    Parametro: 
        -texto_capitalizar (str) : Una cadena que contiene el texto que se escribirá en mayúsculas

    retorno: 
        texto_capitalizado(str) : una cadena con todas las palabras de la cadena de entrada en mayúsculas.
    """

    capitalizados = []
    texto_capitalizado = ""
    # dividir el texto en una lista de palabras
    palabras = texto_capitalizar.split()
    for palabra in palabras:
        capitalizada = palabra.capitalize()  # capitalizar cada palabra en la lista
        capitalizados.append(capitalizada)
    # unir las palabras capitalizadas en un solo string con espacios entre ellas
    texto_capitalizado = " ".join(capitalizados)

    return texto_capitalizado
# 1.7


def obtener_nombre_capitalizado(heroe: dict) -> str:
    """
    Esta función toma un diccionario que contiene el nombre de un héroe y devuelve la versión en
    mayúsculas del nombre con una etiqueta.

    Parametro:
      -heroe (dict): un diccionario que contiene información sobre un héroe, incluido su nombre

    Retorno: 
        -resultado : Una cadena que incluye el nombre en mayúscula de un héroe.
    """
    nombre = heroe['nombre']
    nombre_capitalizado = capitalizar_palabras(nombre)
    resultado = "Nombre: {0}".format(nombre_capitalizado)
    return resultado


def obtener_dato(heroe: dict, key: str) -> str:
    """
    Esta función toma un diccionario y una clave como entrada y devuelve el valor asociado con la clave
    en una cadena formateada o un mensaje si no se encuentra la clave.

    Parametros: 
        -heroe(dicc): un diccionario que contiene información sobre un héroe
        -key(str) : una cadena que representa la clave de un valor específico en un diccionario. 

    Retorno: 
        una cadena que incluye la clave en mayúsculas y el valor correspondiente del diccionario
        héroe, o un mensaje que indica que no se encontraron los datos si la clave no está presente en el
        diccionario.
    """
    dato = heroe[key]
    key_capitalizada = capitalizar_palabras(key)
    if dato:
        return '{0} : {1}'.format(key_capitalizada, dato)
    else:
        return 'No se encontró el dato'

# 1.8


def obtener_nombre_y_dato(heroe: dict, key: str):
    """
    La función toma un diccionario y una clave como entrada y devuelve una cadena formateada que
    contiene el nombre en mayúsculas del diccionario y el valor asociado con la clave dada, o un mensaje
    que indica que no se encontró la clave.

    Parametros: 
        -heroe(dict): un diccionario que contiene información sobre un héroe
        -key(str) : una cadena que representa la clave de un valor específico a buscar en un diccionario. 


    Retorno:
    una cadena que concatena el nombre en mayúscula de un héroe y un valor de datos específico
    de un diccionario. Si hubo un error la función devuelve una cadena que incluye el nombre y un mensaje
    que indica que no se encontraron los datos.
    """

    nombre = obtener_nombre_capitalizado(heroe)
    dato = obtener_dato(heroe, key)

    if nombre and dato:
        return '{0} | {1}'.format(nombre, dato)
    else:
        return '{} | Dato no encontrado'.format(nombre)

# 2 Segunda Parte
# 2.1


def es_genero(heroe: dict, genero: str) -> bool:
    """
    La función comprueba si el género de un héroe determinado coincide con un género específico y
    devuelve un valor booleano en consecuencia.

    Parametros:
        -heroe(dict): un diccionario que represente a un héroe, que debe tener una clave 
        'genero' que indique el género del héroe.
        -genero(str): el genero (ya sea "M" para hombre o "F" para mujer)

    Retorno:
        un valor booleano (Verdadero o Falso) dependiendo de si la clave 'genero' en el diccionario
        de entrada 'heroe' coincide con la cadena de entrada 'genero'. Si la clave no está presente o no
        coincide, la función devuelve False.
    """

    if 'genero' in heroe:
        if heroe['genero'] == genero:
            return True
    return False

# 2.2


def stark_guardar_heroe_genero(lista_heroes: list[dict], genero: str) -> bool:
    """
    Esta función guarda una lista de héroes con un género específico en un archivo CSV.

    Parametros:
        lista_heroes (list[dict]) : una lista de diccionarios que contienen información sobre diferentes héroes
       -genero(str): el genero (ya sea "M" para hombre o "F" para mujer)

    :return: 
        -un valor booleano : True si se guardo de lo contrario False.
    """

    heroes_genero = []
    for heroe in lista_heroes:
        if es_genero(heroe, genero):
            nombre = obtener_nombre_capitalizado(heroe)
            heroes_genero.append(nombre)
            imprimir_dato(nombre)

    nombres = '\n'.join(heroes_genero)

    nombre_archivo = './starks/heroes_{0}.csv'.format(genero)

    return guardar_archivo(nombre_archivo, nombres)

# 3  Tercera Parte

# 3.1


def calcular_min_genero(lista: list[dict], key: str, genero: str) -> dict:
    """
    Esta función calcula el héroe con el valor mínimo para una clave dada
    entre los héroes de un géneroespecífico en una lista dada.

    parametro:
        -lista una lista de diccionarios que representan héroes.
        -key(str) : La clave es una cadena que representa el atributo del héroe.
        -genero(str): el genero (ya sea "M" para hombre o "F" para mujer)

    Retorno: 
        min_heroe(dict) : un diccionario que contiene el héroe con el valor
        mínimo para la clave especificada entre
        los héroes del género especificado en la lista de entrada. Si la lista de 
        entrada está vacía o nohay héroes del género especificado en la lista,
        se devuelve un diccionario vacío.
    """
    min_heroe = {}
    if not lista:
        return min_heroe
    primer_heroe = None

    for heroe in lista:
        if es_genero(heroe, genero):
            primer_heroe = heroe
            break

    if primer_heroe is None:
        return min_heroe

    min_valor = primer_heroe[key]
    min_heroe = primer_heroe

    for heroe in lista:
        if es_genero(heroe, genero) and heroe[key] < min_valor:
            min_valor = heroe[key]
            min_heroe = heroe
    return min_heroe

# 3.2


def calcular_max_genero(lista, key, genero: str):
    """
    Esta función calcula el héroe con el valor max para una clave dada
    entre los héroes de un géneroes pecífico en una lista dada.

    parametro:
        -lista una lista de diccionarios que representan héroes.
        -key(str) : La clave es una cadena que representa el atributo del héroe.
       -genero(str): el genero (ya sea "M" para hombre o "F" para mujer)

    Retorno: 
        max_heroe(dict) : un diccionario que contiene el héroe con el valor
        maximo para la clave especificada entre
        los héroes del género especificado en la lista de entrada. Si la lista de 
        entrada está vacía o nohay héroes del género especificado en la lista,
        se devuelve un diccionario vacío.
    """
    max_heroe = {}

    if not lista:
        return max_heroe
    primer_heroe = None

    for heroe in lista:
        if es_genero(heroe, genero):
            primer_heroe = heroe
            break

    if primer_heroe is None:
        return max_heroe

    max_valor = primer_heroe[key]
    max_heroe = primer_heroe

    for heroe in lista:
        if es_genero(heroe, genero) and heroe[key] > max_valor:
            max_valor = heroe[key]
            max_heroe = heroe
    return max_heroe

# 3.3




def calcular_max_min_dato_genero(lista_heroes: list[dict], tipo_calculo:str, key_dato: str, genero: str) -> dict:
    """
    La función calcula el valor máximo o mínimo de una clave de datos específica para un género dado en
    una lista de diccionarios que contienen información sobre héroes.
    
    Parametros:
        -lista_heroes Una lista de diccionarios que contienen información sobre superhéroes.
        -tipo_calculo una cadena que indica si se debe calcular el valor máximo o mínimo de los datos
        -key_dato Este parámetro es una cadena que representa la clave de los datos para los que
        queremos calcular el valor máximo o mínimo.
        -genero(str): el genero (ya sea "M" para hombre o "F" para mujer)
    Retorno:
        max_min: un diccionario que contiene el valor máximo o mínimo, sino hubo errores de lo
        contrario devuelve un diccionario vacío.
    """

    max_min = {}
    if tipo_calculo == "maximo" and key_dato in lista_heroes[0]:
        max_min = calcular_max_genero(lista_heroes, key_dato, genero)

    elif tipo_calculo == "minimo" and key_dato in lista_heroes[0]:
        max_min = calcular_min_genero(lista_heroes, key_dato, genero)

    else:

        print("Todo mal!")
    return max_min
# 3.4


def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes: list, max_min: str, key: str, genero: str) -> bool:
    """
    Calcula el héroe con el máximo o mínimo valor en una key específica para un género determinado. Luego imprime el resultado
    y guarda en un archivo CSV el héroe obtenido.
    Parámetros:
    - lista_heroes: list. Una lista de diccionarios con información de héroes.
    - max_min: str. String que puede tomar los valores "maximo" o "minimo", según se desee buscar el valor máximo o mínimo.
    - key: str. La llave del diccionario sobre la que se desea realizar la búsqueda.
   -genero(str): el genero (ya sea "M" para hombre o "F" para mujer)
    Retorna:
    - bool. True si se guardó el archivo exitosamente, False si no.
    """

    heroe_obtenido = calcular_max_min_dato_genero(
        lista_heroes, max_min, key, genero)
    heroe_obtenido = obtener_nombre_y_dato(heroe_obtenido, key)
    imprimir_dato(heroe_obtenido)

    nombre_archivo = "./starks/heroes_{0}_{1}_{2}.csv".format(
        max_min, key, genero)
    return guardar_archivo(nombre_archivo, heroe_obtenido)

# 4 Cuarta Parte

# 4.1


def sumar_dato_heroe_genero(lista_heroes: list[dict], key: str, genero: str) -> int:
    """
    Esta función toma una lista de diccionarios que representan superhéroes, una clave y un género, y
    devuelve la suma de los valores de la clave dada para todos los superhéroes del género dado, o -1 si
    no hay superhéroes de ese género.
    
    Parametros:
        -lista_heroes (list[dict]): Una lista de diccionarios, donde cada diccionario es un solo superhéroe.
        -key(str) :La clave es una cadena que representa el atributo del héroe que queremos sumar. 
        -genero(str): el genero (ya sea "M" para hombre o "F" para mujer)
    
    Retorno: 
      suma(int): un valor entero, que es la suma de los valores de la clave en ese genero,o 
      -1 si no hay héroes en la lista que coincidan con los criterios.
    """
  
    suma = 0

    for heroe in lista_heroes:
        if type(heroe) is dict and len(heroe) > 0 and es_genero(heroe, genero):
            if key == "altura" or key == "peso" or key == "fuerza":
                suma += heroe[key]
    if suma > 0:
        return suma
    else:
        return -1

# 4.2


def cantidad_heroes_genero(lista_heroes: list[dict], genero: str):
    """
    La función cuenta el número de héroes en una lista de diccionarios que coinciden con un género
    determinado.
    
    parametros: 
        -lista_heroes (list[dict]): Una lista de diccionarios, donde cada diccionario es un solo superhéroe.
        -genero(str): el genero (ya sea "M" para hombre o "F" para mujer)
    
    Retorno:
        -contador(int):el número de héroes en una lista dada de diccionarios que coinciden con un género
    específico sino se puedo contar devulve un 0.
    """
    contador = 0

    for heroe in lista_heroes:
        if es_genero(heroe, genero):
            contador += 1

    return contador

# 4.3


def calcular_promedio(lista_heroes: list[dict], dato_calcular: str, genero: str) -> float:
    """
    Esta función calcula el promedio de un atributo de datos específico para una lista determinada de
    héroes en función de su género.
    
    parametros: 
        -lista_heroes (list[dict]): Una lista de diccionarios, donde
        cada diccionario es un solo superhéroe.
        -dato_calcular(str) :La clave es una cadena que representa el
        atributo del héroe que queremos calcular el promedio..
        -genero(str): el genero (ya sea "M" para hombre o "F" para mujer)
 
    Retorno: 
        -promedio: un valor flotante que representa el promedio o un 0 si hubo un error.
    """

    suma = 0
    promedio = 0
    if lista_heroes:
        suma = sumar_dato_heroe_genero(lista_heroes, dato_calcular, genero)
        print("la suma es: {0}".format(suma))
        cantidad = cantidad_heroes_genero(lista_heroes, genero)
        print("la cantidad es: {0}".format(cantidad))
        promedio = dividir(suma, cantidad)
        print("el promedio es : {0}".format(promedio))

    return promedio


def dividir(dividendo: int, divisor: int) -> float:
    """
    La función divide dos números y devuelve el resultado, o 0 si el divisor es 0.
    
    Parametros: 
        -dividendo(int) : El número que se está dividiendo.
        -divisor(int) : El número que divide el dividendo en la operación de división.
    
    Retorno:  
        el resultado de dividir el 'dividendo' por el 'divisor' como un flotante, a menos que el
        'divisor' sea 0, en cuyo caso devuelve 0.
    """

    if divisor == 0:
        return 0
    else:
        resultado = dividendo / divisor
    return resultado

# 4.4


def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes:list[dict], genero: str):
    """
    Esta función calcula y guarda la altura promedio de los héroes de un género específico de una lista
    de héroes dada.
    
    Parametros: 
        -lista_heroes (list[dict]): Una lista de diccionarios, donde
        cada diccionario es un solo superhéroe.
        -genero(str): el genero (ya sea "M" para hombre o "F" para mujer)
    
    Retorno:  
    un valor booleano, ya sea Verdadero o Falso, dependiendo de si el archivo se guardó
    correctamente o no.
    """


    promedio_altura = 0
    if lista_heroes:
        promedio_altura = calcular_promedio(lista_heroes, "altura", genero)
        mensaje = "Altura promedio género {0} : {1:.2f}".format(
            genero, promedio_altura)
    else:
        mensaje = "Error: Lista de héroes vacía. "
    imprimir_dato(mensaje)
    archivo_promedio_altura = './starks/heroes_promedio_altura_{}.csv'.format(
        genero)

    datos = 'genero: {0}, promedio_altura: {1}'.format(genero, promedio_altura)
    return guardar_archivo(archivo_promedio_altura, datos)

# 5 Quinta Parte

# 5.1


def calcular_cantidad_tipo(lista_heroes: list[dict], tipo: str) -> dict:
    """
    Esta función toma una lista de héroes y un tipo de atributo de héroe como entrada y devuelve un
    diccionario con el recuento de cada valor único para ese atributo.

    Parametros: 
        -lista_heroes (list[dict]): Una lista de diccionarios, donde
        cada diccionario es un solo superhéroe.
        -tipo una cadena que representa el tipo de información que se extraerá de la lista de héroes.
        Esta función toma una lista de diccionarios, donde cada diccionario representa un héroe y contiene
        información diversa sobre ellos, como nombre, poderes y afiliaciones. El parámetro "tipo" especifica
        qué tipo de información extraer, como
    
    Retorno  
        -un diccionario que contiene el recuento de héroes según el tipo especificado. Si la lista de
        entrada está vacía, devuelve un diccionario con un mensaje de error.
    """

    diccionario = {}

    if lista_heroes:
        for heroe in lista_heroes:
            valor = heroe[tipo]
            if valor != '':
                valor = capitalizar_palabras(valor)
            else:
                valor = 'No Tiene'

            if valor in diccionario:
                diccionario[valor] += 1
            else:
                diccionario[valor] = 1
    else:
        diccionario = {"Error": 'La lista se encuentra vacía'}

    return diccionario

# 5.2



def guardar_cantidad_heroes_tipo(diccionario, tipo_dato):
    """
    Esta función guarda la cantidad de héroes de cierto tipo en un diccionario en un archivo CSV.
    
    @param diccionario Un diccionario que contiene información sobre los héroes y sus características.
    @param tipo_dato El tipo de datos de los héroes, como "poderes" o "habilidades".
    
    @return un valor booleano, ya sea Verdadero o Falso, dependiendo de si el archivo se guardó
    correctamente o no.
    """
    contenido = ''
    for key, value in diccionario.items():
        mensaje = "Caracteristica: {0} {1} - Cantidad de heroes: {2}\n".format(
            tipo_dato, key, value)
        imprimir_dato(mensaje)
        contenido += mensaje

    archivo = "./starks/heroes_cantidad_{0}.csv".format(tipo_dato)

    if guardar_archivo(archivo, contenido):
        return True
    else:
        return False

# 5.3


def stark_calcular_cantidad_por_tipo(heroes, tipo):
    """
    Esta función calcula la cantidad de héroes por tipo dado y guarda el resultado.
    
    @param heroes una lista de diccionarios que representan superhéroes, donde cada diccionario contiene
    información sobre un solo superhéroe, como su nombre, poderes y tipo (por ejemplo, "héroe" o
    "villano").
    @param tipo El parámetro "tipo" es una cadena que representa el tipo de héroe para el que queremos
    calcular la cantidad. Se utiliza en las funciones "calcular_cantidad_tipo" y
    "guardar_cantidad_heroes_tipo" para determinar qué héroes contar y cómo almacenar el resultado.
    
    @return the result of the function call to `guardar_cantidad_heroes_tipo(cantidad_heroes, tipo)`.
    """

    cantidad_heroes = calcular_cantidad_tipo(heroes, tipo)
    guardado = guardar_cantidad_heroes_tipo(cantidad_heroes, tipo)
    return guardado

# 6  Sexta Parte
# 6.1


def obtener_lista_de_tipos(heroes, tipo):
    """
    Esta función toma una lista de héroes y un tipo de héroe y devuelve una lista de valores únicos en
    mayúsculas para ese tipo de héroe.
    
    @param heroes una lista de diccionarios que representan diferentes héroes, donde cada diccionario
    contiene información sobre un héroe como su nombre, tipo, habilidades, etc.
    @param tipo El tipo de atributo de héroe para el que queremos obtener una lista de valores únicos.
    Por ejemplo, si queremos obtener una lista de valores únicos para el atributo "clase" de los héroes,
    pasaríamos "clase" como el valor de tipo.
    
    @return una lista de valores únicos en mayúsculas para un tipo determinado de héroe en una lista de
    héroes. El tipo de héroe se especifica mediante el parámetro "tipo".
    """

    valores_tipo_actualizados = []
    for heroe in heroes:
        valor = heroe[tipo]
        if not valor:
            valor_normalizado = normalizar_dato(valor, 'N/A')
        else:
            valor_normalizado = valor
        valor_capitalizado = capitalizar_palabras(valor_normalizado)
        valores_tipo_actualizados.append(valor_capitalizado)

    valores_tipo_unicos = []
    for valor in valores_tipo_actualizados:
        if valor not in valores_tipo_unicos:
            valores_tipo_unicos.append(valor)

    return valores_tipo_unicos

# 6.2


def normalizar_dato(dato, default):
    """
    La función normaliza datos dados reemplazándolos con un valor predeterminado si los datos están
    vacíos o son nulos.
    
    @param dato Los datos de entrada que deben normalizarse.
    @param default El valor predeterminado para usar si la entrada `dato` está vacía o Ninguno.
    
    @return el valor normalizado de la entrada "dato". Si "dato" está vacío o Ninguno, se reemplazará
    por el valor predeterminado y luego se devolverá.
    """


    if not dato:
        dato = default

    return dato

# 6.3


def normalizar_heroe(heroe, key):
    """
    Esta función normaliza los datos de un héroe poniendo en mayúscula su nombre y normalizando el valor
    de una clave específica.
    
    @param heroe un diccionario que contiene información sobre un superhéroe
    @param key El parámetro "clave" es una cadena que representa la clave de un atributo específico en
    un diccionario. Esta clave se utiliza para acceder al valor correspondiente en el diccionario
    "heroe" que se pasa como argumento a la función "normalizar_heroe". La función luego normaliza el
    valor de
    
    @return un diccionario que contiene los datos normalizados de un héroe, con el nombre del héroe en
    mayúscula y el valor de una clave específica también en mayúscula y normalizado.
    """

    heroe_normalizado = {}

    if 'nombre' in heroe:
        heroe_normalizado['nombre'] = capitalizar_palabras(heroe['nombre'])

    if key in heroe:
        valor = heroe[key]
        valor = normalizar_dato(valor, 'N/A')
        heroe_normalizado[key] = capitalizar_palabras(valor)

    return heroe_normalizado

# 6.4


def obtener_heroes_por_tipo(heroes, tipos, tipo_dato):
    """
    Esta función toma una lista de héroes, una lista de tipos y un tipo de datos, y devuelve un
    diccionario de héroes agrupados por sus respectivos tipos según el tipo de datos dado.
    
    @param heroes una lista de diccionarios que representan diferentes héroes, cada uno con varios
    atributos como nombre, tipo y habilidades.
    @param tipos una lista de cadenas que representan los diferentes tipos de héroes (por ejemplo,
    "tanque", "apoyo", "daño")
    @param tipo_dato una cadena que representa el tipo de datos que se normalizarán para cada héroe (por
    ejemplo, "rol" o "afinidad")
    
    @return un diccionario donde las claves son los tipos de héroes especificados en el parámetro
    `tipos`, y los valores son listas de nombres de héroes que pertenecen a cada tipo.
    """

    heroes_por_tipo = {}

    for tipo in tipos:
        heroes_por_tipo[tipo] = []

    for heroe in heroes:
        valor_tipo = normalizar_heroe(heroe, tipo_dato)
        # Obtener el nombre del héroe del diccionario normalizado
        nombre = valor_tipo['nombre']
        for tipo in tipos:
            if valor_tipo[tipo_dato] == tipo:
                heroes_por_tipo[tipo].append(nombre)

    return heroes_por_tipo

# 6.5


def guardar_heroes_por_tipo(diccionario_tipos_nombres: dict, tipo_dato: str) -> bool:
    """
    Esta función toma un diccionario de tipos y nombres de héroes, y una cadena de tipos de datos, y
    guarda los héroes agrupados por su tipo en un archivo CSV.
    
    @param diccionario_tipos_nombres Un diccionario que contiene nombres de héroes categorizados por su
    tipo.
    @param tipo_dato una cadena que representa el tipo de datos que se almacenan
    
    @return un valor booleano.
    """
 

    contenido = ""

    for key, valor in diccionario_tipos_nombres.items():
        if len(valor) > 0:
            nombres_heroes = ",".join(valor)
            mensaje = "{} {}: {}\n".format(tipo_dato, key, nombres_heroes)
            imprimir_dato(mensaje)
            contenido += mensaje

    archivo = "./starks/heroes_segun_{0}.csv".format(tipo_dato)
    return guardar_archivo(archivo, contenido)

# 6.6

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
