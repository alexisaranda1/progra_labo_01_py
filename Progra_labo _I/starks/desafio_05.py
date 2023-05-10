import re
import json
import csv

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')
def stark_normalizar_datos(heroes: list[dict]) -> None:
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
    if heroes:
        # Recorro cada diccionario de heroe de la lista
        for heroe in heroes:
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
    '''Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla, 
    el cual permite utilizar toda la funcionalidad ya programada. 
    Se deberá reutilizar la función antes creada encargada de imprimir un string (1.2)
    '''
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
    imprimir_menu_Desafio_5()
    opcion = input("Ingrese una opcion: ").upper()
    if re.match('[A-OZ]{1}', opcion):
        return opcion    
    return -1
 #1.2   
def imprimir_dato(cadena_caracteres: str):
    '''Crear la función 'imprimir_dato' la cual recibirá por parámetro un string
    y deberá imprimirlo en la consola.
    La función no tendrá retorno.'''
    if type(cadena_caracteres) == str:
        print(cadena_caracteres)
    else:
        print("No es una cadena de texto")

#1.4
def leer_archivo(ruta: str):

    with open(ruta, 'r') as archivo:
        contenido = json.load(archivo)
        lista_heroes = contenido['heroes']
    return lista_heroes

#1.5
def guardar_archivo(nombre_archivo:str, lista:list): 

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:

        for heroe in lista:
            mensaje = "{0},{1},{2},{3},{4},{5}\n"

            mensaje = mensaje.format(   heroe["nombre"].replace(",","-").replace("\n","@"),
                                        heroe["identidad"].replace(",","-").replace("\n","@"),
                                        heroe["empresa"].replace(",","-").replace("\n","@"),
                                        heroe["altura"].replace(",","-").replace("\n","@"),
                                        heroe["peso"].replace(",","-").replace("\n","@"),
                                        heroe["genero"].replace(",","-").replace("\n","@"),
                                        heroe["color_ojos"].replace(",","-").replace("\n","@"),
                                        heroe["color_pelo"].replace(",","-").replace("\n","@"),
                                        heroe["fuerza"].replace(",","-").replace("\n","@"),
                                        heroe["inteligencia"].replace(",","-").replace("\n","@")
                                        
                                        
                                        )
            
            archivo.write(mensaje)

#1.3

def stark_marvel_app ():
    # ruta = r"C:\Users\Axex Shop\Desktop\progra_labo_01\progra_labo_01_py\Progra_labo _I\starks\data_stark.json"
    # leer_archivo(ruta)
    while True:
        opcion = stark_menu_principal_desafio_5()
        match opcion:
            case "A":
                print("A ")
            case "B":
                 print("B ")
            case "C":
                 print("C ")
            case "D":
                print("D")
            case "E":
               print("E")
            case "F":
                print("F")
            case "G":
               print("G")
            case "H":
                 print("H")
            case "I":
                print("I")
            case "J":
                print("J")
            case "K":
                print("K")
            case "L":
                print("L")      
            case "M":
                print("M")
            case "N":
                print("N")                    
            case "O":
                print(("o"))
            case "Z":
                print("salio!")
                break
            case _:
                print("¡opción incorrecta!.")

#1.6

def capitalizar_palabras(texto: str):

    capitalizados = []
    palabras = texto.split()  # dividir el texto en una lista de palabras
    for palabra in palabras:
        capitalizada = palabra.capitalize()  # capitalizar cada palabra en la lista
        capitalizados.append(capitalizada)

    return " ".join(capitalizados)  # unir las palabras capitalizadas en un solo string con espacios entre ellas

#1.7

def obtener_nombre_capitalizado(heroe: dict) -> str:

    nombre = heroe['nombre']
    nombre_capitalizado = capitalizar_palabras(nombre)
    resultado = "Nombre: {0}".format(nombre_capitalizado)
    return resultado

def obtener_dato(heroe: dict, key: str) -> str:
    dato = heroe[key]
    if dato:
        return dato
    else:
        return 'No se encontró el dato'

#1.8

def obtener_nombre_y_dato(heroe: dict, key: str) -> str:

    nombre = obtener_nombre(heroe)
    dato = obtener_dato(heroe, key)
    
    key_capitalizada = capitalizar_palabras(key)
    if nombre and dato:
        return '{} | {}: {}'.format(nombre, key_capitalizada, dato)
    else:
        return '{} | Dato no encontrado'.format(nombre)

# 2 Segunda Parte
#2.1    

def es_genero(heroe: dict, genero: str) -> bool:

    if 'genero' in heroe:
        if heroe['genero'] == genero :
            return True
    return False
    
# 3  Tercera Parte

#3.1

def calcular_min_genero(lista, key, genero : str):
    
    if not lista:
        return None
    primer_heroe = None

    for heroe in lista:
        if heroe['genero'] == genero:
            primer_heroe = heroe
            break
        
    if primer_heroe is None:
        return None

    min_valor = primer_heroe[key]
    min_heroe = primer_heroe

    for heroe in lista:
        if heroe['genero'] == genero and heroe[key] < min_valor:
            min_valor = heroe[key]
            min_heroe = heroe
    return min_heroe

#3.2

def calcular_max_genero(lista, key, genero: str):
    
    if not lista:
        return None
    primer_heroe = None
    
    for heroe in lista:
        if heroe['genero'] == genero:
            primer_heroe = heroe
            break

    if primer_heroe is None:
        return None

    max_valor = primer_heroe[key]
    max_heroe = primer_heroe

    for heroe in lista:
        if heroe['genero'] == genero and heroe[key] > max_valor:
            max_valor = heroe[key]
            max_heroe = heroe
    return max_heroe

#3.3

def calcular_max_min_dato(lista_heroes, tipo_calculo, key_dato , genero: str):
    
    if tipo_calculo == "maximo" and key_dato in lista_heroes[0]:
        maximo = calcular_max_genero(lista_heroes, key_dato, genero)
        return maximo
    elif tipo_calculo == "minimo" and key_dato in lista_heroes[0]:
        minimo = calcular_min_genero(lista_heroes, key_dato, genero)
        return minimo 
    else:

        prin("Todo mal!")

ruta = r"progra_labo_01_py\Progra_labo _I\starks\data_stark.json"

lista_personaje = leer_archivo(ruta)

archivo_nuevo = "datos.csv" 
guardar_archivo(archivo_nuevo, lista_personaje)

stark_normalizar_datos(lista_personaje)

print(calcular_max_min_dato(lista_personaje,"minimo","altura", "F" ))


