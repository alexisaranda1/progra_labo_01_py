import random
import time
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
# def menu(lista_personajes)-> None:
#     pass


def ordenar_por_clave(lista, flag_orden, clave):
    rango_a = len(lista) - 1
    flag_swap = True

    while flag_swap:
        flag_swap = False

        for indice_A in range(rango_a):
            if (flag_orden == False and lista[indice_A][clave] < lista[indice_A+1][clave]) \
                    or (flag_orden == True and lista[indice_A][clave] > lista[indice_A+1][clave]):
                
                lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                flag_swap = True

                
def guardar_archivo(nombre_archivo:str, contenido)-> bool:


    with open(nombre_archivo, 'w+') as archivo:
        resultado = None
        resultado = archivo.write(contenido)
    if resultado:
        print("Se creó el archivo: {0}".format(nombre_archivo))
        return True

    print("Error al crear el archivo: {0}".format(nombre_archivo))
    return False



ruta = r"starks\data_stark.json"
lista_personajes = leer_archivo(ruta)
















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