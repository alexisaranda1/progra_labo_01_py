
import json

import  os
def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

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



 
def ordenar_por_clave(lista_heroes : list[dict], clave: str, flag_orden : bool)-> list:
    """
    La función ordena una lista de diccionarios por una clave específica en orden ascendente o
    descendente.
    
    Parametros
        -lista_heroes:  Una lista de diccionarios que representan héroes.
        -clave:  El parámetro "clave" es una cadena que representa la clave o atributo del diccionario
        que se utilizará para ordenar la lista de diccionarios.
        -flag_orden: El parámetro flag_orden es un indicador booleano que determina si la lista debe
        ordenarse en orden ascendente o descendente según el valor de la clave especificada. 
    Retorno:
        -La función `ordenar_por_clave` devuelve una lista ordenada de diccionarios basada en una
        clave específica y orden de clasificación.
    """
    lista = lista_heroes[:]
    rango_a = len(lista) - 1
    flag_swap = True 

    while flag_swap:
        flag_swap = False

        for indice_A in range(rango_a):
            if (flag_orden == True and lista[indice_A][clave] < lista[indice_A+1][clave]) \
                    or (flag_orden == False and lista[indice_A][clave] > lista[indice_A+1][clave]):
                
                lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                flag_swap = True
    return lista
def ordenar_largo_nombre(lista_heroes : list[dict], clave: str, flag_orden : bool)-> list:
    """
    La función ordena una lista de diccionarios por una clave específica en orden ascendente o
    descendente.
    
    Parametros
        -lista_heroes:  Una lista de diccionarios que representan héroes.
        -clave:  El parámetro "clave" es una cadena que representa la clave o atributo del diccionario
        que se utilizará para ordenar la lista de diccionarios.
        -flag_orden: El parámetro flag_orden es un indicador booleano que determina si la lista debe
        ordenarse en orden ascendente o descendente según el valor de la clave especificada. 
    Retorno:
        -La función `ordenar_por_clave` devuelve una lista ordenada de diccionarios basada en una
        clave específica y orden de clasificación.
    """
    lista = lista_heroes[:]
    rango_a = len(lista) - 1
    flag_swap = True 

    while flag_swap:
        flag_swap = False

        for indice_A in range(rango_a):
            if (flag_orden == True and len(lista[indice_A][clave]) < len(lista[indice_A+1][clave])) \
                    or (flag_orden == False and len(lista[indice_A][clave]) > len(lista[indice_A+1][clave])):
                
                lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                flag_swap = True
    return lista
                
def guardar_archivo(nombre_archivo:str, contenido)-> bool:
    """
    Esta función guarda el contenido dado en un archivo con el nombre especificado y devuelve un valor
    booleano que indica si la operación se realizó correctamente.
    
    @param nombre_archivo Una cadena que representa el nombre del archivo que se va a crear o
    sobrescribir.
    @param contenido El contenido que se escribirá en el archivo. Puede ser una cadena o cualquier otro
    tipo de datos que se pueda convertir en una cadena.
    
    @return un valor booleano que indica si el archivo se creó correctamente o no. Se devuelve True si
    el archivo se creó correctamente y se devuelve False si hubo un error al crear el archivo.
    """

    with open(nombre_archivo, 'w+') as archivo:
        resultado = None
        resultado = archivo.write(contenido)
    if resultado:
        print("Se creó el archivo: {0}".format(nombre_archivo))
        return True

    print("Error al crear el archivo: {0}".format(nombre_archivo))
    return False

def imprimir_menu_Desafio_6()-> None:
    """
    Esta función imprime un menú con diferentes opciones.
    """
    menu = '''\n\t------------------- Menu---------------------------------------\n
            1)Crear una función llamada ‘ordenar_por_altura’ 
            que reciba como parámetro la lista de héroes y 
            devuelva la lista ordenada por la altura de cada 
            personaje de menor a mayor
            2)Crear una función llamada ‘ordenar_por_peso’ 
            que reciba como parámetro la lista de héroes y devuelva
            la lista ordenada por el peso de cada personaje mayor a mayor. 
            3)Crear una función llamada ‘ordenar_por_nombre’ que reciba 
            como parámetro la lista de héroes y la devuelva la lista de 
            héroes ordenada por nombres de forma alfabética ascendente 
            (de la A a la Z)
            4)Crear una función llamada ‘ordenar_por_largo_nombre’ que
            reciba como parámetro la lista de héroes y la devuelva la
            lista de héroes ordenada por el largo del nombre
            de forma descendente
            5)Crear una función llamada ‘ordenar_por_key’ la misma recibirá tres parámetros: 
            La lista de héroes Un string que represente el nombre de una key
            Un booleano que represente el sentido de ordenamiento (por defecto debe tomar el valor True)
            La función deberá ordenar la lista de personajes según la key especificada.
            El sentido de ordenamiento lo determina el tercer parámetro, en caso de ser True 
            el orden va a ser ascendente (de menor a mayor)
            y en el caso de ser False el sentido es descendente (mayor a menor)
        '''
    imprimir_dato(menu)
def imprimir_dato(cadena_caracteres: str)-> None:

    """
    La función "imprimir_dato" comprueba si la entrada es una cadena y la imprime, de lo contrario,
    imprime un mensaje diciendo que no es una cadena.
    
    Parametro:
        -cadena_caracteres(str): una variable de tipo cadena que representa una secuencia de caracteres.
    """
    if type(cadena_caracteres) == str:
        print(cadena_caracteres)
    else:
        print("No es una cadena de texto")


ruta = r"starks\data_stark.json"
lista_personajes = leer_archivo(ruta)
stark_normalizar_datos(lista_personajes) 

while True:
    imprimir_menu_Desafio_6()
    opcion =int( input("ingrese una opcion: "))
    match opcion:
        case 1:
            lista_ordanada_altura = ordenar_por_clave(lista_personajes,"altura", False)
            for heroe in lista_ordanada_altura:
                print("Nombre : {0} y altura {1}".format(heroe["nombre"], heroe["altura"]))
        case 2:
            lista_ordanada_peso = ordenar_por_clave(lista_personajes,"peso", True)
            for heroe in lista_ordanada_peso:
                print("Nombre : {0} y peso {1}".format(heroe["nombre"], heroe["peso"]))
        case 3:
            lista_ordanada_nombre = ordenar_por_clave(lista_personajes,"nombre", False)
            for heroe in lista_ordanada_nombre:
                print("Nombre : {0}".format(heroe["nombre"]))
        case 4:
            lista_ordanada_nombre_largo = ordenar_largo_nombre(lista_personajes,"nombre", False)
            for heroe in lista_ordanada_nombre_largo:
                print("Nombre : {0}".format(heroe["nombre"]))
            pass
        case 5:
            lista_ordanada_altura = ordenar_por_clave(lista_personajes,"fuerza", False)
            for heroe in lista_ordanada_altura:
                print("Nombre : {0} y altura {1}".format(heroe["nombre"], heroe["fuerza"]))
        case 6:
            print('salio del programa!')
            break
        case _:
            print('Error no disponible.')
    clear_console()
    

























# def ivan_sort_B(lista:list[dict],flag_orden:bool, key):
#     rango_a = len(lista) - 1
#     flag_swap = True

#     while(flag_swap):
#         flag_swap = False

#         for indice_A in range(rango_a):
#             if  flag_orden == False and lista[indice_A] < lista[indice_A+1] \
#              or flag_orden == True and lista[indice_A] > lista[indice_A+1]:
#                 lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
#                 flag_swap = True


# def ivan_sort_A(lista:list):
#     rango_a = len(lista)
#     flag_swap = True

#     while(flag_swap):
#         flag_swap = False
#         rango_a = rango_a - 1

#         for indice_A in range(rango_a):
#             if  lista[indice_A] < lista[indice_A+1]:
#                 lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
#                 flag_swap = True



# lista = list(range(10000))
# random.shuffle(lista)

# lista_A = lista[:]
# lista_B = lista[:]
# lista_C = lista[:]


# inicio = time.time()
# ivan_sort_A(lista_A)
# fin = time.time()

# print("IVAN_A {0}".format((fin-inicio)))


# inicio = time.time()
# ivan_sort_B(lista_B,True)
# fin = time.time()

# print("IVAN_B {0}".format((fin-inicio)))



# inicio = time.time()
# ivan_sort_A(lista_A)
# fin = time.time()

# print("IVAN_A_YA ORDENADO {0}".format((fin-inicio)))

