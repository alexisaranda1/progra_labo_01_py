
from data_stark import lista_personajes

import os
def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

#0
def stark_normalizar_datos(heroes: list[dict]) -> None:
    '''Recorrer la lista y convertir al tipo de dato correcto las keys (solo con las keys que representan datos numéricos)
    Validar primero que el tipo de dato no sea del tipo al cual será casteado. Por ejemplo si una key debería ser entero (ejemplo edad) verificar antes que no se encuentre ya en ese tipo de dato.
    Si al menos un dato fue modificado, la función deberá imprimir como mensaje ‘Datos normalizados’, caso contrario no imprimirá nada.
    Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
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

#1.2
def imprimir_dato(cadena_caracteres: str):
    '''Crear la función 'imprimir_dato' la cual recibirá por parámetro un string
    y deberá imprimirlo en la consola.
    La función no tendrá retorno.'''

    if type(cadena_caracteres) == str:
        print(cadena_caracteres)
    else:
        print("No es una cadena de texto")

#1.3
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

#1.4
def obtener_dato(heroe: dict, key):
    dato = heroe[key]
    if dato:
        return dato
    else:
        print("No es un dato valido")

#2
def obtener_nombre_y_dato(heroe: dict, key: str) -> str:
    ''' Crear la función 'obtener_nombre_y_dato' la misma recibirá por 
    parámetro un diccionario el cual representara a un héroe y una key (string)
    la cual representará el dato que se desea obtener. 

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

#3

def stark_imprimir_nombres_alturas(lista_heroes: list):
    """Crear la función 'stark_imprimir_nombres_alturas' 
    la cual recibirá por parámetro la lista de héroes, la cual deberá 
    iterar e imprimir sus nombres y alturas USANDO la función creada en el punto 2.
    Validar que la lista de héroes no esté vacía para realizar sus acciones, 
    caso contrario no hará nada y retornara -1."""

    if lista_heroes:
        for heroe in lista_heroes:
            nombre_altura_obtenido = obtener_nombre_y_dato(heroe, "altura")
            imprimir_dato(nombre_altura_obtenido)
    else:
        return -1

#4.1


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


#4.2


def calcular_min(lista, key):
    min_valor = lista[0][key]
    min_heroe = lista[0]

    for i in range(len(lista)):
     
        if lista[i][key] < min_valor:
            min_valor = lista[i][key]
            min_heroe = lista[i]

    return min_heroe


#4.3


def calcular_max_min_dato(lista_heroes, tipo_calculo, key_dato):
    
    if tipo_calculo == "maximo" and key_dato in lista_heroes[0]:
        maximo = calcular_max(lista_heroes, key_dato)
        return maximo
    elif tipo_calculo == "minimo" and key_dato in lista_heroes[0]:

        minimo = calcular_min(lista_heroes, key_dato)
       # print(minimo["altura"])
        return minimo 
    else:
        print("todo mal!")
        
            
#4.4

def stark_calcular_imprimir_heroe (lista_heroes: list , max_min : str, key : str) :
    '''La lista de héroes
El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.'''
    if lista_heroes:
        
       heore_obtenido =  calcular_max_min_dato(lista_heroes, max_min, key)
       heore_obtenido = obtener_nombre_y_dato(heore_obtenido,key)
       imprimir_dato(heore_obtenido)
       
    else:
        return -1
    
    
#5.1
def sumar_dato_heroe(lista_heroes, key):
    
    '''Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de 
    héroes y un string que representara el dato/key de los héroes que se requiere sumar. 
    Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes 
    de hacer la suma. La función deberá retorna la suma de todos los datos según la key
    pasada por parámetro'''
    
    suma = 0
    
    for heroe in lista_heroes:
        
        if type(heroe) is dict and len(heroe) > 0 :
            
            if key == "altura" or key == "peso" or key == "fuerza" :
            
                suma += heroe[key]
            else:
                print("Dato key!!")   
        else :
            
            return 0
        
    return suma
#5.2
def dividir(dividendo, divisor):
    
    '''Crear la función  ‘dividir’ la cual recibirá como parámetro dos números 
    (dividendo y divisor). Se debe verificar si el divisor es 0,  en caso de serlo, 
    retornar 0, caso contrario realizar la división entre los parámetros y retornar
    el resultado'''
    
    print("numero dividendo: {0}".format(dividendo))
    if divisor == 0:
        return 0
    else:
        resultado = dividendo / divisor
        
    return resultado


#5.3
def calcular_promedio(lista_heroes, dato_calcular):
    '''crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de héroes
    y un string que representa el dato del héroe que se requiere calcular el promedio.
    La función debe retornar el promedio del dato pasado por parámetro'''
    
    suma = 0
    cantidad = len(lista_heroes)
    
    if cantidad > 0:
        suma = sumar_dato_heroe(lista_heroes, dato_calcular)
        promedio = dividir(suma, cantidad )
    else :
        
        return 0
            
    promedio = suma / cantidad
    
    return promedio


#5.4
def stark_calcular_imprimir_promedio_altura(lista_heroes):
    '''Crear la función 'stark_calcular_imprimir_promedio_altura' 
la cual recibirá una lista de héroes y utilizando la función del punto 5.3
calcula y mostrará la altura promedio. Validar que la lista de héroes no 
esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.'''

    if lista_heroes :
        
        promedio_altura = calcular_promedio(lista_heroes,"altura")

        # promedio_altura_string = "Promedio altura es : {0}".format(promedio_altura)
        # imprimir_dato(promedio_altura_string)
  
        print("Promedio altura es : {0}".format(promedio_altura))
        
    else:
        return -1
    
    
#6.1
def imprimir_menu():
    
    '''Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla, 
    el cual permite utilizar toda la funcionalidad ya programada. 
    Se deberá reutilizar la función antes creada encargada de imprimir un string (1.2)
    '''
    imprimir_dato('\t1) Imprimir nombres :\n\t2) Imprimir Nombre y Altura :'
                  '\n\t3) cacular maximo Fuerza  \n\t 4) Calular promedio Altura:')


#6.2

def validar_entero(cadena_numeros: str) -> bool:
    '''Crear la función “validar_entero” la cual recibirá 
por parámetro un string de número el cual deberá verificar
que sea sea un string conformado únicamente por dígitos. 
Retornara True en caso de serlo, False caso contrario
'''
    return cadena_numeros.isdigit()
 
#6.3

def stark_menu_principal(max_intentos=3):
    imprimir_menu()
    contador_intentos = 0
    opcion = input("Ingrese el número de una opción: ")
    

    while contador_intentos < max_intentos:
        if validar_entero(opcion) and int(opcion) in range(1, 5):
            return int(opcion)
        else:
            contador_intentos += 1
            
            if contador_intentos == max_intentos:
                return -1
            else:
                print("Opción inválida. Intento {0}/{1}".format(contador_intentos, max_intentos))
                imprimir_menu()
                opcion = input("Ingrese el número de una opción: ")

#7

def stark_marvel_app (lista_personajes):
    
    '''Crear la función 'stark_marvel_app' la cual recibirá por parámetro 
    la lista de héroes y se encargará de la ejecución principal de nuestro programa. 
     Debe informar por consola en caso de seleccionar una 
    opción incorrecta y volver a pedir el dato al usuario. Reutilizar
    las funciones con prefijo 'stark_' donde crea correspondiente.'''
    
    stark_normalizar_datos(lista_personajes)
    
    while True:
        opcion = stark_menu_principal()
        
        match opcion:
        
            case 1:
                stark_imprimir_nombres_heroes(lista_personajes)
            case 2:
                stark_imprimir_nombres_alturas(lista_personajes)
            case 3:
                stark_calcular_imprimir_heroe(lista_personajes, "maximo", "fuerza") 
            case 4:
                stark_calcular_imprimir_promedio_altura(lista_personajes)
            case -1:
                print("Salio")
                break
            
        clear_console()


#main 

stark_marvel_app(lista_personajes)
   
