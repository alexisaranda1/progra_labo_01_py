import json

def leer_archivo_csv(nombre_archivo: str)-> list:

    lista = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            print(linea)
            lista_campos = linea.split(",")
            heroe = {}
            heroe["nombre"] = lista_campos[0]
            heroe["edad"] = lista_campos[1]
            heroe["feurza"] = lista_campos[2]
            heroe["inteligencia"] = lista_campos[3]
            heroe["empresa"] = lista_campos[4]
            heroe["apodo"] = lista_campos[5]
            lista.append(heroe)

    return lista

def leer_archivo_sjon(ruta: str) -> list:
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


def guardar_archivo_csv(nombre_archivo: str, contenido: str) -> bool:
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
    
    if nombre_archivo is str and  contenido is str: 
        with open(nombre_archivo, 'w+') as archivo:
            resultado = None # 
            resultado = archivo.write(contenido)
        if resultado:
            print("Se creó el archivo: {0}".format(nombre_archivo))
            return True

    print("Error al crear el archivo: {0}".format(nombre_archivo))
    return False

def guardar_archivo_json(nombre_archivo:str, lista:list):
    """
    Esta función toma un nombre de archivo y una lista como entrada, crea un diccionario con la lista
    como valor y lo guarda como un archivo JSON con el nombre de archivo dado.
    
    @param nombre_archivo Una cadena que representa el nombre del archivo que se creará o sobrescribirá
    con los datos JSON.
    @param lista El parámetro "lista" es una lista que contiene los datos que deben guardarse en un
    archivo JSON.
    """
    if nombre_archivo is str and lista: 
        dict_json = {}
        dict_json["heroes"] = lista
        with open(nombre_archivo, "w+") as archivo:
            json.dump(dict_json, archivo, indent=4)
            print(dict_json['horoes'])       


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