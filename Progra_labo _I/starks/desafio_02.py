import os
from data_stark import lista_personajes


def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')


def stark_normalizar_datos(heroes: list[dict]) -> None:

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
                            print(f'El dato {key} fue modificada para el heroe: {heroe["nombre"]}')
    else:
        print('Error La lista esta vacía.')


def obtener_nombre(heroe):
    '''Crear la función 'obtener_nombre' la cual recibirá por parámetro
    un diccionario el cual representara a un héroe y devolverá un string 
    el cual contenga su nombre 
    formateado de la siguiente manera:'''
    nombre = heroe['nombre']

    if len(nombre) != 0:
        return 'Nombre: {}'.format(nombre)

    else:
        return "Nombre no encontrado"


def imprimir_dato(cadena_caracteres: str):
    '''Crear la función 'imprimir_dato' la cual recibirá por parámetro un string
    y deberá imprimirlo en la consola.
    La función no tendrá retorno.'''

    if type(cadena_caracteres) == str:
        print(cadena_caracteres)
    else:
        print("No es una cadena de texto")


def stark_imprimir_nombres_heroes(lista_heroes: list):
    '''Crear la función 'stark_imprimir_nombres_heroes'
    la cual recibirá por parámetro la lista de héroes y 
    deberá imprimirla en la consola. Reutilizar las funciones hechas 
    en los puntos 1.1 y 1.2. 
    Validar que la lista no esté vacía '''

    if not lista_heroes:
        print("Error: Lista de héroes vacía")
        return -1
    for heroe in lista_heroes:
        nombre = obtener_nombre(heroe)
        imprimir_dato(nombre)


def obtener_dato(heroe: dict, key):
    dato = heroe[key]
    if dato:
        return dato
    else:
        print("No es un dato valido")


def obtener_nombre_y_dato(heroe: dict, key: str) -> str:
    ''' Crear la función 'obtener_nombre_y_dato' la misma recibirá por 
    parámetro un diccionario el cual representara a un héroe y una key (string) la cual representará el dato que se desea obtener. 

    La función deberá devolver un string el cual contenga 
    el nombre y dato (key) del héroe a imprimir. El dato puede ser 
    'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.

    El string resultante debe estar formateado de la siguiente
    manera: (suponiendo que la key es fuerza)
    Nombre: Venom | fuerza: 500
    '''

    nombre = obtener_nombre(heroe)
    dato = obtener_dato(heroe, key)

    if nombre and dato:
        return '{} | {}: {}'.format(nombre, key, dato)
    else:
        return '{} | Dato no encontrado'.format(nombre)


def stark_imprimir_nombres_alturas(lista_heroes: list):
    """Crear la función 'stark_imprimir_nombres_alturas' 
    la cual recibirá por parámetro la lista de héroes, la cual deberá 
    iterar e imprimir sus nombres y alturas USANDO la función creada en el punto 2.
    Validar que la lista de héroes no esté vacía para realizar sus acciones, 
    caso contrario no hará nada y retornara -1."""

    if lista_heroes:
        for heroe in lista_heroes:
            nombre_altura_obtenido = obtener_nombre_y_dato(heroe, "altura")
            print(nombre_altura_obtenido)
    else:
        return -1


def calcular_max(lista, key):
    if not lista:
        return None

    max_valor = lista[0][key]
    max_heroe = lista[0]

    for i in range(len(lista)):
        # for heroe in lista[1:]:
        if lista[i][key] > max_valor:
            max_valor = lista[i][key]
            max_heroe = lista[i]
    return max_heroe


def calcular_min(lista, key):
    min_valor = lista[0][key]
    min_heroe = lista[0]

    for i in range(len(lista)):
        # for heroe in lista[1:]:
        if lista[i][key] < min_valor:
            min_valor = lista[i][key]
            min_heroe = lista[i]

    return min_heroe


def calcular_max_min_dato(lista_heroes, tipo_calculo, key_dato):
    if tipo_calculo == "maximo" and key_dato in lista_heroes[0]:
        maximo = calcular_max(lista_heroes, key_dato)
        return maximo
    elif tipo_calculo == "minimo" and key_dato in lista_heroes[0]:

        minimo = calcular_min(lista_heroes, key_dato)
        print(minimo["altura"])
        return minimo 
    else:
        print("todo mal!")

#main 

stark_normalizar_datos(lista_personajes)





stark_imprimir_nombres_heroes(lista_personajes)

stark_imprimir_nombres_alturas(lista_personajes)
