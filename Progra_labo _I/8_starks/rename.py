import re
import json





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
                            #verificar si el valor de la clave key 
                            #contiene exactamente un punto en su interior
                            heroe[key] = float(heroe[key])
                        else:
                            heroe[key] = int(heroe[key])
                            #print(f'El dato {key} fue modificada para el heroe: {heroe["nombre"]}')
    else:
        print('Error La lista esta vacía.')
        
#1.1

  
def imprimir_menu_Desafio_5():
    """
    Esta función imprime un menú con diferentes opciones.
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

#1.2

def stark_menu_principal_desafio_5():
    """
    Esta función muestra un menú y solicita al usuario que ingrese una opción, devolviendo la opción si
    coincide con un patrón determinado o -1 de lo contrario.
    
    @return Si la entrada del usuario coincide con el patrón de expresión regular '[A-OZ]{1}', la
    función devolverá la cadena de entrada en mayúsculas. De lo contrario, devolverá -1.
    """
    imprimir_menu_Desafio_5()
    opcion = input("Ingrese una opcion: ").upper()
    if re.match('[A-OZ]{1}', opcion):
        return opcion    
    return -1
 #1.2   
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

#1.4
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

# #1.5 
def guardar_archivo(nombre_archivo:str, contenido)-> bool:


    with open(nombre_archivo, 'w+') as archivo:
        resultado = None
        resultado = archivo.write(contenido)
    if resultado:
        print("Se creó el archivo: {0}".format(nombre_archivo))
        return True

    print("Error al crear el archivo: {0}".format(nombre_archivo))
    return False




# def guardar_archivo(nombre_archivo:str, lista:list) -> bool:
#     """
#     La función guarda una lista de diccionarios que contienen información de héroes en un archivo CSV.
    
#     @param nombre_archivo Una cadena que representa el nombre del archivo que se va a crear o
#     sobrescribir.
#     @param lista Una lista de diccionarios con información sobre héroes.
    
#     @return un valor booleano, True si el archivo se creó correctamente y False en caso contrario.
#     """
#     """
#     Guarda una lista de diccionarios en un archivo CSV.
#     Parámetros:
#     - nombre_archivo: str. El nombre del archivo a crear o sobrescribir.
#     - lista: list. Una lista de diccionarios con información de héroes.
#     Retorna:
#     - bool. True si se creó el archivo exitosamente, False si no.
#     """

#     with open(nombre_archivo, "w", encoding="utf-8") as archivo:
#         resultado = None
#         for heroe in lista:
#             print(heroe['nombre'])
#             mensaje = "{0},{1},{2},{3},{4},{5}\n"
#             print(heroe['nombre'])
#             mensaje = mensaje.format(   heroe["nombre"].replace(",","-").replace("\n","."),
#                                         heroe["identidad"].replace(",","-").replace("\n","."),
#                                         heroe["empresa"].replace(",","-").replace("\n","."),
#                                         heroe["altura"].replace(",","-").replace("\n","."),
#                                         heroe["peso"].replace(",","-").replace("\n","."),
#                                         heroe["genero"].replace(",","-").replace("\n","."),
#                                         heroe["color_ojos"].replace(",","-").replace("\n","."),
#                                         heroe["color_pelo"].replace(",","-").replace("\n","."),
#                                         heroe["fuerza"].replace(",","-").replace("\n","."),
#                                         heroe["inteligencia"].replace(",","-").replace("\n","."))
#             resultado = archivo.write(mensaje)
    
#         if resultado:
#             print("Se creó el archivo: {0}".format(nombre_archivo))
#             return True
    
#         print("Error al crear el archivo: {0}".format(nombre_archivo))
#         return False

#aca va el mach

#1.6

def capitalizar_palabras(texto: str):
    """
    La función escribe en mayúscula la primera letra de cada palabra en una cadena dada.
    
    @param texto una cadena de texto que contiene una o más palabras separadas por espacios.
    
    @return una cadena con todas las palabras de la cadena de entrada en mayúsculas.
    """
    capitalizados = []
    palabras = texto.split()  # dividir el texto en una lista de palabras
    for palabra in palabras:
        capitalizada = palabra.capitalize()  # capitalizar cada palabra en la lista
        capitalizados.append(capitalizada)

    return " ".join(capitalizados)  # unir las palabras capitalizadas en un solo string con espacios entre ellas

#1.7

def obtener_nombre_capitalizado(heroe: dict) -> str:
    """
    Esta función toma un diccionario que contiene el nombre de un héroe y devuelve el nombre con cada
    palabra en mayúscula.
    
    @param heroe Un diccionario que contiene información sobre un héroe, incluido su nombre.
    
    @return una cadena que incluye el nombre en mayúscula de un héroe, precedido por la palabra
    "Nombre:".
    """

    nombre = heroe['nombre']
    nombre_capitalizado = capitalizar_palabras(nombre)
    resultado = "Nombre: {0}".format(nombre_capitalizado)
    return resultado

def obtener_dato(heroe: dict, key: str) -> str:
    """
    La función toma un diccionario y una clave como entrada y devuelve el valor de la clave en una
    cadena formateada o un mensaje si no se encuentra la clave.
    
    @param heroe Un diccionario que contiene información sobre un héroe.
    @param key La clave es una cadena que representa los datos específicos que queremos obtener del
    diccionario héroe. Se utiliza para acceder al valor asociado a esa clave en el diccionario.
    
    @return una cadena que incluye la clave en mayúsculas y el valor correspondiente del diccionario
    héroe, o un mensaje que indica que no se encontraron los datos si la clave no está presente en el
    diccionario.
    """
    dato = heroe[key]
    key_capitalizada = capitalizar_palabras(key)
    if dato:
        return '{0} : {1}'.format(key_capitalizada,dato)
    else:
        return 'No se encontró el dato'

#1.8

def obtener_nombre_y_dato(heroe: dict, key: str) :
    """
    Esta función toma un diccionario que representa un héroe y una clave, y devuelve una cadena con el
    nombre en mayúsculas del héroe y el valor asociado con la clave, o un mensaje que indica que no se
    encontraron los datos.
    
    @param heroe Un diccionario que representa a un héroe, con claves que representan diferentes
    atributos del héroe (por ejemplo, nombre, edad, poderes, etc.) y valores que representan los valores
    correspondientes de esos atributos.
    @param key El parámetro clave es una cadena que representa la clave del valor que queremos obtener
    del diccionario del héroe.
    
    @return una cadena que concatena el nombre en mayúscula de un héroe y un valor de datos específico
    de un diccionario, separados por un símbolo de canalización. Si el nombre o el valor de los datos no
    se encuentran en el diccionario, la función devuelve una cadena que indica que no se encontraron los
    datos.
    """
    
    nombre = obtener_nombre_capitalizado(heroe)
    dato = obtener_dato(heroe, key)
  
    if nombre and dato:
        return '{0} | {1}'.format(nombre, dato)
    else:
        return '{} | Dato no encontrado'.format(nombre)

# 2 Segunda Parte
#2.1    

def es_genero(heroe: dict, genero: str) -> bool:
    """
    La función comprueba si el género de un héroe determinado coincide con un género específico y
    devuelve un valor booleano.
    
    @param heroe un diccionario que representa un personaje de superhéroe, que puede contener una clave
    'genero' que indica el género del personaje
    @param genero El parámetro "genero" es una cadena que representa el género que queremos buscar en el
    diccionario de héroes.
    
    @return un valor booleano (Verdadero o Falso) dependiendo de si la clave 'genero' en el diccionario
    de entrada 'heroe' coincide con la cadena de entrada 'genero'. Si la clave no está presente o no
    coincide, la función devuelve False.
    """

    if 'genero' in heroe:
        if heroe['genero'] == genero :
            return True
    return False

#2.2
def stark_guardar_heroe_genero(lista_heroes: list [dict], genero: str) -> bool:
    """
    Esta función toma una lista de héroes y un género como entrada, filtra los héroes por género, guarda
    los héroes filtrados en un archivo CSV y devuelve un valor booleano que indica si el archivo se
    guardó correctamente.
    
    @param lista_heroes una lista de héroes, donde cada héroe se representa como un diccionario con las
    claves 'nombre' (nombre), 'genero' (género) y 'poderes' (poderes)
    @param genero El parámetro "genero" es una cadena que representa el género de los héroes que
    queremos filtrar y guardar en un archivo CSV. Puede tener tres valores posibles: "M" para héroes
    masculinos, "F" para héroes femeninos y "NB" para héroes no binarios.
    
    @return un valor booleano, que es el resultado de llamar a la función `guardar_archivo` con los
    argumentos `nombre_archivo` y `heroes_genero`.
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

#3.1

def calcular_min_genero(lista, key, genero : str) -> dict :
    """
    Esta función calcula el héroe con el valor mínimo para una clave dada entre los héroes de un género
    específico en una lista dada.
    
    @param lista una lista de diccionarios que representan superhéroes
    @param key El parámetro clave es una cadena que representa el atributo del objeto héroe que queremos
    comparar y encontrar el valor mínimo.
    @param genero El parámetro "genero" es una cadena que representa el género del héroe. Se usa para
    filtrar la lista de héroes y solo considerar aquellos que coinciden con el género especificado.
    
    @return La función `calcular_min_genero` devuelve el héroe con el valor mínimo para la clave dada
    entre todos los héroes en la lista de entrada que tienen el género especificado. Si no hay héroes
    con el género especificado en la lista, devuelve "Ninguno".
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
        if  es_genero(heroe, genero) and heroe[key] < min_valor:
            min_valor = heroe[key]
            min_heroe = heroe
    return min_heroe

#3.2

def calcular_max_genero(lista, key, genero: str):
    """
    La función calcula el héroe con el valor máximo para una clave dada entre los héroes de un género
    específico en una lista dada.
    
    @param lista una lista de diccionarios que representan superhéroes
    @param key El parámetro clave es una cadena que representa el atributo del objeto héroe que queremos
    comparar para encontrar el valor máximo. Por ejemplo, si queremos encontrar al héroe con la fuerza
    más alta, estableceríamos la clave en "fuerza".
    @param genero El parámetro "genero" es una cadena que representa el género del héroe. Se usa para
    filtrar la lista de héroes y solo considerar aquellos que coinciden con el género especificado.
    
    @return La función `calcular_max_genero` devuelve el héroe con el valor más alto para la clave dada
    entre los héroes del género especificado en la lista de entrada. Si no hay héroes del género
    especificado en la lista, devuelve "Ninguno".
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

#3.3

def calcular_max_min_dato_genero(lista_heroes, tipo_calculo, key_dato , genero: str)-> dict:
    """
    Esta función calcula el valor máximo o mínimo de una clave de datos específica para un género dado
    en una lista de héroes.
    
    @param lista_heroes una lista de diccionarios que contienen información sobre superhéroes
    @param tipo_calculo una cadena que indica si se debe calcular el valor máximo o mínimo
    @param key_dato una cadena que representa la clave de los datos a calcular (por ejemplo,
    "inteligencia", "fuerza", etc.)
    @param genero una cadena que representa el género de los héroes a considerar en los cálculos.
    
    @return ya sea el valor máximo o mínimo de una clave de datos específica para un género dado en una
    lista de héroes, dependiendo del valor del parámetro "tipo_calculo". Si el parámetro "key_dato" no
    está presente en el primer elemento del parámetro "lista_heroes", la función imprime "¡Todo mal!" y
    no devuelve nada.
    """
    # The above code is not a valid Python code. It seems to be a random word or a comment.
    max_min = {}
    if tipo_calculo == "maximo" and key_dato in lista_heroes[0]:
        max_min = calcular_max_genero(lista_heroes, key_dato, genero)

    elif tipo_calculo == "minimo" and key_dato in lista_heroes[0]:
        max_min = calcular_min_genero(lista_heroes, key_dato, genero)
       
    else:

        print("Todo mal!")
    return max_min 
#3.4

def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes: list, max_min: str, key: str, genero: str) -> bool:
    """
    Calcula el héroe con el máximo o mínimo valor en una key específica para un género determinado. Luego imprime el resultado
    y guarda en un archivo CSV el héroe obtenido.
    Parámetros:
    - lista_heroes: list. Una lista de diccionarios con información de héroes.
    - max_min: str. String que puede tomar los valores "maximo" o "minimo", según se desee buscar el valor máximo o mínimo.
    - key: str. La llave del diccionario sobre la que se desea realizar la búsqueda.
    - genero: str. String que representa el género a evaluar.
    Retorna:
    - bool. True si se guardó el archivo exitosamente, False si no.
    """

    heroe_obtenido = calcular_max_min_dato_genero(lista_heroes, max_min, key, genero)
    heroe_obtenido = obtener_nombre_y_dato(heroe_obtenido, key)
    imprimir_dato(heroe_obtenido)

    nombre_archivo = "./starks/heroes_{0}_{1}_{2}.csv".format(max_min, key, genero)
    return guardar_archivo(nombre_archivo, heroe_obtenido)

#4 Cuarta Parte

#4.1

def sumar_dato_heroe_genero (lista_heroes: list[dict], key:str, genero: str )-> int:
    """
    Esta función calcula la suma de un atributo específico (altura, peso o fuerza) para todos los héroes
    de un género determinado en una lista de diccionarios.
    
    @param lista_heroes una lista de diccionarios que representan superhéroes
    @param key El parámetro clave es una cadena que representa el atributo del héroe que queremos
    resumir. Puede ser "altura" (altura), "peso" (peso) o "fuerza" (fuerza).
    @param genero una cadena que representa el género de los héroes a considerar en el cálculo
    
    @return la suma de los valores de la clave especificada ("altura", "peso" o "fuerza") para todos los
    héroes en la lista de entrada que coincidan con el género especificado. Si no hay héroes en la lista
    que coincidan con el género o si la entrada no tiene el formato esperado, la función devuelve -1.
    """
    suma = 0

    for heroe in lista_heroes:
        if type(heroe) is dict and len(heroe) > 0 and es_genero(heroe, genero):
            if key == "altura" or key == "peso" or key == "fuerza" :
                suma += heroe[key]
        else :
            return -1
    return suma

#4.2
def cantidad_heroes_genero(lista_heroes : list[dict], genero: str): 
    """
    La función cuenta el número de héroes en una lista de diccionarios que coinciden con un género
    determinado.
    
    @param lista_heroes una lista de diccionarios que representan superhéroes, donde cada diccionario
    contiene información sobre un solo superhéroe, como su nombre, género, poderes, etc.
    @param genero El parámetro "genero" es una cadena que representa el género de los héroes que
    queremos contar en el parámetro "lista_heroes".
    
    @return el número de héroes en una lista dada de diccionarios que coinciden con un género
    específico.
    """
    contador = 0
   
    for heroe in lista_heroes:
        if es_genero(heroe , genero):
            contador += 1

    return contador

#4.3

def calcular_promedio(lista_heroes, dato_calcular, genero) -> float:
    """
    Esta función calcula el promedio de un atributo de datos específico para un género dado entre una
    lista de héroes.
    
    @param lista_heroes Es una lista de objetos de héroe que contiene información sobre cada héroe, como
    su nombre, género, poderes, etc.
    @param dato_calcular Los datos a calcular para cada héroe, como su fuerza o nivel de inteligencia.
    @param genero género de los héroes (por ejemplo, "masculino", "femenino", "no binario")
    
    @return el promedio calculado (promedio) de un dato dado (dato_calcular) para un género específico
    (genero) entre una lista de héroes (lista_heroes). Si la lista está vacía, devuelve 0.
    """
    suma = 0
    promedio = 0
    if lista_heroes:
        suma = sumar_dato_heroe_genero(lista_heroes, dato_calcular, genero)
        cantidad = cantidad_heroes_genero(lista_heroes, genero)
        promedio = dividir(suma, cantidad)

            
    return promedio

def dividir(dividendo, divisor)-> float: 
    """
    La función divide dos números y devuelve el resultado, pero si el divisor es cero, devuelve cero.
    
    @param dividendo El dividendo, o el número que se divide.
    @param divisor El divisor es un número que se usa para dividir el dividendo en la función. No puede
    ser cero, ya que dividir por cero no está definido.
    
    @return La función `dividir` devuelve el resultado de dividir `dividendo` entre `divisor`, a menos
    que `divisor` sea igual a 0, en cuyo caso devuelve 0.
    """
    if divisor == 0:
        return 0
    else:
        resultado = dividendo / divisor 
    return resultado
#4.4
def stark_calcular_imprimir_guardar_promedio_altura_genero (lista_heroes, genero):
    """
    Esta función calcula e imprime la altura promedio de los héroes de un género determinado de una
    lista y guarda el resultado en un archivo CSV.
    
    @param lista_heroes una lista de diccionarios que contienen información sobre superhéroes, incluida
    su altura y género.
    @param genero género (en español)
    
    @return un valor booleano, ya sea Verdadero o Falso, dependiendo de si el archivo se guardó
    correctamente o no.
    """
    
    promedio_altura = 0
    if lista_heroes :
        promedio_altura = calcular_promedio(lista_heroes,"altura", genero)
        mensaje = "Altura promedio género {0} : {1:.2f}".format(genero, promedio_altura)
    else:
        mensaje = "Error: Lista de héroes vacía. "
    imprimir_dato(mensaje)
    archivo_promedio_altura = './starks/heroes_promedio_altura_{}.csv'.format(genero)

    datos = 'genero: {0}, promedio_altura: {1}'.format(genero, promedio_altura)
    if guardar_archivo(archivo_promedio_altura,datos):
        return True
    else :
        return False
    
#5 Quinta Parte
#5.1 
def calcular_cantidad_tipo (lista_heroes, key ):
    """
    Esta función toma una lista de héroes y una clave, y devuelve un diccionario con el recuento de cada
    tipo de héroe según la clave dada.
    
    @param lista_heroes una lista de diccionarios que representan héroes, donde cada diccionario
    contiene información sobre un héroe, como su nombre, poderes y tipo.
    @param key El parámetro "clave" es una cadena que representa la clave del diccionario que se
    utilizará para agrupar a los héroes por tipo. Por ejemplo, si la clave es "tipo", la función
    agrupará a los héroes por su atributo "tipo" y devolverá un diccionario con el recuento de cada
    tipo.
    
    @return un diccionario que contiene el recuento de cada tipo de héroe en la lista de entrada de
    héroes. Si la lista de entrada está vacía, la función devuelve un diccionario con un mensaje de
    error.
    """
    diccionario = {}

    if lista_heroes:

        for heroe in lista_heroes:
            tipo = heroe[key]
            tipo = capitalizar_palabras(tipo)
            if tipo in diccionario:
                diccionario[tipo] += 1
            else:
                diccionario[tipo] = 1
    else :

        diccionario= {"Error": 'La lista se encuentra vacía'}

    return diccionario
#5.2
def guardar_cantidad_heroes_tipo(diccionario, tipo_dato):
    """
    Esta función guarda la cantidad de héroes para cada característica de un tipo de datos dado en un
    archivo CSV.
    
    @param diccionario Un diccionario que contiene las características de los héroes y su
    correspondiente cantidad.
    @param tipo_dato una cadena que representa el tipo de datos que se analizan (por ejemplo, "poderes",
    "habilidades", "nacionalidades")
    
    @return Un valor booleano que indica si el archivo se guardó correctamente o no.
    """
    mensaje = ''
    for key, value in diccionario.items():
        mensaje += "Caracteristica: {0} {1} - Cantidad de heroes: {2}\n".format(tipo_dato, key, value)

    archivo = f"heroes_cantidad_{tipo_dato}.csv"
    if guardar_archivo(archivo, mensaje):
        return True
    else:
        return False
#5.3
def stark_calcular_cantidad_por_tipo(heroes, tipo):
    """
    Esta función calcula la cantidad de héroes por tipo y guarda el resultado en un archivo CSV.
    
    @param heroes Es una lista de diccionarios que contienen información sobre diferentes héroes. Cada
    diccionario representa a un héroe y contiene claves como "nombre", "tipo", "poder", etc.
    @param tipo El parámetro "tipo" es una cadena que representa el tipo de héroe para el que queremos
    calcular la cantidad. Se utiliza en la función para crear un nombre de archivo para el archivo CSV
    que se guardará con los resultados.
    
    @return the result of the function call to `guardar_cantidad_heroes_tipo(cantidad_heroes, tipo,
    nombre_archivo)`.
    """
    cantidad_heroes = calcular_cantidad_tipo(heroes, tipo)
    guardado = guardar_cantidad_heroes_tipo(cantidad_heroes, tipo )
    return guardado

# 6  Sexta Parte
#6.1

# def obtener_lista_de_tipos(heroes : list[dict], tipo: str)-> list:
#     """
#     Esta función toma una lista de héroes y un tipo, y devuelve una lista de valores únicos para ese
#     tipo, con la primera letra de cada palabra en mayúscula.
    
#     @param heroes una lista de diccionarios que representan diferentes héroes, donde cada diccionario
#     contiene información sobre un héroe, como su nombre, poderes y tipo.
#     @param tipo El parámetro "tipo" es una cadena que representa la clave del diccionario que contiene
#     el tipo de cada héroe en la lista de "héroes".
    
#     @return una lista de valores únicos para un tipo dado de héroe en la lista de entrada de héroes, con
#     cualquier valor vacío reemplazado con "N/A" y con cada valor en mayúscula usando la función
#     capitalizar_palabras.
#     """
#     valores_tipo = []

#     for heroe in heroes:
#         valor = heroe[tipo]
#         if not valor:
#             valor = "N/A"
#         valores_tipo.append(valor)

#     valores_tipo = set(valores_tipo)
#     valores_tipo.discard("")
#     for valor in valores_tipo:
#         valor_capitalizado = capitalizar_palabras(valor)
#         valores_tipo.append(valor_capitalizado)


#     return valores_tipo
#6.2
def normalizar_dato(dato, default):
    """
    La función normaliza un dato dado reemplazándolo con un valor predeterminado si está vacío o es
    nulo.
    
    @param dato Los datos de entrada que deben normalizarse.
    @param default El valor predeterminado que se devolverá si el parámetro de entrada 'dato' está vacío
    o es Ninguno.
    
    @return el valor normalizado de la entrada "dato". Si "dato" está vacío o Ninguno, se reemplazará
    por el valor predeterminado proporcionado como parámetro. Luego se devuelve el valor final de
    "dato".
    """

    if not dato:
       dato= default
    
    return dato
#6.3

def normalizar_heroe(heroe, key):
    """
    Esta función normaliza el valor del atributo de un héroe poniendo en mayúsculas las palabras y
    reemplazando los valores faltantes con "N/A".
    
    @param heroe El diccionario de héroes que contiene información sobre un héroe, como su nombre, poder
    y otros atributos.
    @param key El parámetro clave es una cadena que representa el atributo del héroe que queremos
    normalizar. Puede ser cualquier atributo como 'edad', 'genero', 'poder', etc.
    
    @return un diccionario con los valores normalizados del nombre del héroe de entrada y la clave
    especificada. El valor de la clave especificada se escribe en mayúscula y se normaliza mediante la
    función `normalizar_dato`, y el nombre del héroe también se escribe en mayúscula.
    """
    
    valor = heroe[key]
    valor = capitalizar_palabras(valor)
    nombre = capitalizar_palabras(heroe['nombre'])
    key = capitalizar_palabras(key)
    valor = normalizar_dato(valor, 'N/A')

    heroe_normalizado = {'nombre': nombre, key: valor}
    return heroe_normalizado
#6.4
def obtener_heroes_por_tipo(heroes, tipos, key):
    """
    Esta función toma una lista de héroes, una lista de tipos y una clave y devuelve un diccionario con
    cada tipo como clave y una lista de nombres de héroes como valor.
    
    @param heroes una lista de diccionarios, donde cada diccionario representa un héroe y contiene
    información como su nombre, tipo y habilidades.
    @param tipos una lista de cadenas que representan los tipos de héroes para filtrar
    @param key La clave es una cadena que representa el atributo del objeto héroe que se utilizará para
    agrupar los héroes por tipo. Por ejemplo, si la clave es "clase", la función agrupará a los héroes
    por su atributo de clase.
    
    @return Un diccionario con cada tipo como clave y una lista de nombres de héroes como valor.
    """
    """
    Retorna un diccionario con cada variedad como key y una lista de nombres como valor.
    """
    diccionario_variedades = {}
    for tipo in tipos:
        diccionario_variedades[tipo] = []
    for heroe in heroes:
        valor_normalizado = normalizar_dato(heroe[key], 'N/A')
        if valor_normalizado in tipos:
            diccionario_variedades[valor_normalizado].append(heroe['nombre'])
    return diccionario_variedades
# 6.5

def guardar_heroes_por_tipo(heroes_por_tipo, tipo_dato):
    """
    Esta función guarda una lista de héroes por tipo en un archivo CSV.
    
    @param heroes_por_tipo un diccionario donde las claves son cadenas que representan tipos de héroes y
    los valores son listas de cadenas que representan los nombres de los héroes que pertenecen a ese
    tipo.
    @param tipo_dato El tipo de datos de los héroes que se guardarán en el archivo CSV.
    
    @return resultado de llamar a la función `guardar_archivo()` con el nombre de archivo
    "heroes_segun_{tipo_dato}.csv" y el contenido de la lista `contenido` como argumentos.
    """
    contenido = []
    contenido.append("TipoDato,Nombre\n")
    
    for tipo, heroes in heroes_por_tipo.items():
        if tipo == tipo_dato:
            for heroe in heroes:
                contenido.append("{},{}\n".format(tipo, heroe))

    archivo = "heroes_segun_{}.csv".format(tipo_dato)

    return guardar_archivo(archivo, contenido)
# #6.6
# def stark_listar_heroes_por_dato(heroes, tipo_dato):
#     """
#     Esta función toma una lista de héroes y un tipo de datos, crea un diccionario de héroes agrupados
#     por ese tipo de datos y devuelve el diccionario.
    
#     @param heroes Este parámetro es probablemente una lista de diccionarios, donde cada diccionario
#     representa un héroe y contiene información sobre ese héroe, como su nombre, poderes y otras
#     características.
#     @param tipo_dato El parámetro "tipo_dato" hace referencia al tipo de datos que queremos utilizar
#     para filtrar y agrupar a los héroes. Por ejemplo, si queremos agrupar a los héroes por su
#     "superpoder", entonces "tipo_dato" sería "superpoder".
    
#     @return resultado de llamar a la función `guardar_heroes_por_tipo` con el argumento
#     `dict_heroes_por_tipo` y `tipo_dato`.
#     """
#     lista_tipos = obtener_lista_de_tipos(heroes, tipo_dato)
#     dict_heroes_por_tipo = obtener_heroes_por_tipo(heroes, lista_tipos, tipo_dato)
#     return guardar_heroes_por_tipo(dict_heroes_por_tipo, tipo_dato)