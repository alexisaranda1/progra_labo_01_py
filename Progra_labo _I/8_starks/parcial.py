import re
import json

def leer_archivo(ruta:str):
    '''
    Esta función lee un archivo json y lo devuelve como una lista.
    
    Parametro:
    ruta: de tipo string. es la ruta en donde se encuentra el archivo JSON a leer.
    
    Devuelve: una lista que posee el contenido del archivo JSON.
    '''
    with open(ruta, 'r') as archivo:
        diccionario = json.load(archivo)
    return diccionario["heroes"]
    
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

def validacion_respuesta_menu(respuesta: str) -> bool:
    '''
    Utiliza el metodo search de REGEX para validad la respuesta ingresada por input del menú.
    ----------
    Parámetro:
    respuesta: tipo string - es la respuesta ingresada por el input del menú.
    ----------
    Devuelve:
    True o False, dependiendo de si re.search logra encontrar una ocurrencia del patrón.
    '''
    busqueda = re.match(r'^[1-6]{1}$', respuesta)
    if busqueda:
        return True
    else:
        return False
    
def listar_N_heroes(lista_heroes: list[dict], cantidad: int)-> int|list:
    """
    Esta función toma una lista de diccionarios que representan héroes y un número entero que representa
    una cantidad deseada y devuelve una lista de los primeros N héroes en la lista original o -1 si la
    lista está vacía o la cantidad deseada excede la longitud de la lista.
    
    @param lista_heroes Una lista de diccionarios que representan héroes.
    @param cantidad cantidad es un parámetro entero que representa el número de héroes que se incluirán
    en la lista de héroes dada.
    
    @return ya sea una lista de diccionarios que contengan el primer número de "cantidad" de héroes de
    la lista de entrada "lista_heroes", o -1 si la lista de entrada está vacía o si la cantidad
    seleccionada excede el número de elementos de la lista.
    """


    if not lista_heroes:
        print("La lista se encuentra vacía.")
        return -1
    elif (len(lista_heroes) < cantidad):
        print("La cantidad seleccionada supera a la cantidad de elementos de la lista.")
        return -1
    else:
        lista_aux = lista_heroes[:]
        lista_N_heroes = []
        contador = 0
        for heroe in lista_aux:
            if contador < cantidad:
                lista_N_heroes.append(heroe)
                contador += 1
        return lista_N_heroes

def ordenar_lista_por_atributo(lista_original:list[dict], atributo: str, orden: str):
    '''
    Genera una lista de heroes ordenada, según su atributo, con el orden solicitado(asc o desc).
    ----------
    Parámetros:
    lista_orginal: tipo list[dict] - La lista de la cual se trabajará, primero generando una copia.
    atributo: tipo string - La key que se utilizará de parámetro para el ordenamiento.
    orden: tipo string - el tipo de ordenamiento que se solicita. (asc o desc)
    ----------
    Devuelve:
    -1: en caso de error, ya sea que la lista está vacía.
    lista: la lista ordenada, ascendente o descendente, según el atributo pedido por parámetro.
    '''
    if not lista_heroes:
        print("La lista se encuentra vacía.")
        return -1
    lista = lista_original[:]
    rango_a = len(lista)
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1
        for indice_A in range(rango_a):
            if orden == "desc": #mayor a menor
                if  lista[indice_A][atributo] < lista[indice_A+1][atributo]:
                    lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                flag_swap = True
            if orden == "asc": #menor a mayor
                if  lista[indice_A][atributo] > lista[indice_A+1][atributo]:
                    lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]    
                flag_swap = True
    return lista

def calcular_promedio(lista_original: list, atributo: str):
    '''
    Calcula el promedio de la suma del valor de la key proporcionada por param, proveniente
    de los dict de la lista solicitada.
    ----------
    Parámetros:
    lista_orginal: tipo list[dict] - La lista de la cual se trabajará, primero generando una copia.
    atributo: tipo string - La key que se utilizará de parámetro para calcular el promedio de la misma.
    ----------
    Devuelve:
    -1: en caso de error, ya sea que la lista está vacía.
    promedio: tipo float - el valor del promedio del atributo(key) pasado por param.
    '''
    contador = 0
    acumulador = 0
    promedio = 0
    if len(lista_original) == 0:
        return -1
    lista = lista_original[:]
    for heroe in lista:
        if atributo in heroe:
            if(type(heroe[atributo]) == type(int()) or type(heroe[atributo]) == type(float())):
                acumulador += heroe[atributo]
                contador += 1
    if contador > 0:
        promedio = acumulador/contador
        return promedio
    
def filtrar_por_promedio(lista_original: list, atributo: str, cond_filtro: str):
    '''
    Genera una lista de heroes, cuyo heroes superen o se encuentren debajo del promedio del atributo pedido por param.
    ----------
    Parámetros:
    lista_orginal: tipo list[dict] - La lista de la cual se trabajará, primero generando una copia.
    atributo: tipo string - La key que se utilizará filtrar por promedio.
    cond_filtro: tipo string - la condición para filtrar la lista(mayor o menor, en este caso del promedio de la key)
    ----------
    Devuelve:
    -1: en caso de error, ya sea que la lista está vacía.
    lista_filtrada: la lista filtrada por promedio, según el atributo(key) y la condición de filtro pasada por param.
    '''
    if len(lista_original) == 0:
        return -1
    lista = lista_original[:]
    lista_filtrada = []
    promedio = calcular_promedio(lista, atributo)
    for heroe in lista:
        if cond_filtro == "mayor":
            if heroe[atributo] > promedio:
                lista_filtrada.append(heroe)
        elif cond_filtro == "menor":
            if heroe[atributo] < promedio:
                lista_filtrada.append(heroe)
    return lista_filtrada

def buscar_heroes_por_inteligencia(lista_original: list, inteligencia: str):
    '''
    Genera una lista de heroes filtrada según la inteligencia requerida por param, evaluado a través de REGEX.
    ----------
    Parámetros:
    lista_orginal: tipo list[dict] - La lista de la cual se trabajará, primero generando una copia.
    inteligencia: tipo string - El valor de la key inteligencia por el cuál se quiere filtrar.
    ----------
    Devuelve:
    -1: en caso de error, ya sea que la lista está vacía.
    -2: en caso de error, ya que el tipo de inteligencia es erróneo o no existe.
    lista_filtrada: la lista filtrada según la inteligencia pasada por param.
    '''    
    if len(lista_original) == 0:
        print("Lista vacía.")
        return -1
    lista = lista_original[:]
    lista_filtrada = []
    busqueda = re.search(r'good|average|high', inteligencia)
    if busqueda:
        for heroe in lista:
            if heroe["inteligencia"] == inteligencia:
                lista_filtrada.append(heroe)
    else:
        print("Tipo dei inteligencia erróneo")
        return -2
    return lista_filtrada

def guardar_csv(lista_original: list, path: str):
    '''
    Genera un archivo .csv que contendrá la información proveniente de la lista pasada por param.
    ----------
    Parámetros:
    lista_orginal: tipo list[dict] - La lista de la cual se trabajará, primero generando una copia.
    path: tipo string - La ruta donde se guardará el archivo .csv
    ----------
    Devuelve:
    -1: en caso de error, ya sea que la lista está vacía.
    '''
    if len(lista_original) == 0:
        print("Lista vacía.")
        return -1
    lista = lista_original[:]
    lista_heroes_string = []
    for heroe in lista:
        dato_heroe = []
        for value in heroe.values():
            dato_heroe.append(str(value))
        dato_heroe_string = ",".join(dato_heroe)
        lista_heroes_string.append(dato_heroe_string)
    datos_para_csv = "\n".join(lista_heroes_string)
    with open(path, "w") as archivo:
        archivo.writelines(datos_para_csv)
        print("el archivo fue creado en {0}".format(path))
        
def generar_menu(): 
    menu = "1- {0}\n2- {1}\n3- {2}\n4- {3}\n5- {4}\n6- {5}\n".format(
    "Listar los primeros N héroes. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)",    
    "Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)",
    "Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)",
    "Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.",
    "Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda. (Usando RegEx)",
    "Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]"    
    )
    return menu

path_JSON = r"starks\data_stark.json"
 
lista_heroes = leer_archivo(path_JSON)

stark_normalizar_datos(lista_heroes)

ultima_lista_generada = []

while True:
    respuesta = input(generar_menu())
    if validacion_respuesta_menu(respuesta):
        match(int(respuesta)):
            case 1:
                cantidad = input("Ingrese la cantidad de heroes a mostrar por pantalla.")
                while not cantidad.isnumeric():
                    cantidad = input("Error, ingrese una cantidad válida.")    
                lista_nueva = listar_N_heroes(lista_heroes, int(cantidad))
                if lista_nueva == -1:
                    cantidad = input("Error, ingrese una cantidad válida.")
                else:
                    print(lista_nueva)
                    ultima_lista_generada = lista_nueva[:]

            case 2:
                ordenamiento = input("Ingrese como quiere ordenar la lista. (asc o desc)")
                busqueda = re.search(r"asc|desc",ordenamiento,re.I)
                while not busqueda:
                    ordenamiento = input("Ingrese correctamente como quiere ordenar la lista. (asc o desc)")
                    busqueda = re.search(r"asc|desc",ordenamiento,re.I)    
                lista_nueva = ordenar_lista_por_atributo(lista_heroes, "altura", ordenamiento)
                print(lista_nueva)
                ultima_lista_generada = lista_nueva[:]

            case 3:
                ordenamiento = input("Ingrese como quiere ordenar la lista. (asc o desc)")
                busqueda = re.search(r"asc|desc",ordenamiento,re.I)
                while not busqueda:
                    ordenamiento = input("Ingrese correctamente como quiere ordenar la lista. (asc o desc)")
                    busqueda = re.search(r"asc|desc",ordenamiento,re.I)    
                lista_nueva = ordenar_lista_por_atributo(lista_heroes, "fuerza", ordenamiento)
                print(lista_nueva)
                ultima_lista_generada = lista_nueva[:]

            case 4:
                atributo = input("ingrese el atributo a chequear.")
                while not isinstance(lista_heroes[0][atributo], (int, float)):
                    atributo = input("Ingrese el atributo númerico a chequear correctamente.")
                cond_filtro = input("Ingrese si quiere filtrar por mayor o menor del promedio.")
                while cond_filtro != "mayor" and cond_filtro != "menor":
                    cond_filtro = input("Ingrese correctamente si quiere filtrar por mayor o menor del promedio.")    
                lista_nueva = filtrar_por_promedio(lista_heroes, atributo, cond_filtro)
                print(lista_nueva)
                ultima_lista_generada = lista_nueva[:]
            
            case 5:
                inteligencia = input("Ingrese la inteligencia a filtrar.")
                lista_nueva = buscar_heroes_por_inteligencia(lista_heroes, inteligencia)
                if lista_nueva == -1:
                    break
                while lista_nueva == -2:
                    inteligencia = input("Ingrese la inteligencia a filtrar.")
                    lista_nueva = buscar_heroes_por_inteligencia(lista_heroes, inteligencia) 
                print(lista_nueva)

            case 6:
                guardar_csv(ultima_lista_generada,"practica\simulacion_parcial\data.csv")


    else:
        print("Opción incorrecta, ingrese una opción nuevamente.")





