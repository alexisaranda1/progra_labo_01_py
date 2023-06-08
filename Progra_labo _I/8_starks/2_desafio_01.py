from data_stark import lista_personajes
'''
 Agregar al código elaborado para cumplir el desafío #01 los siguientes puntos,
 utilizando un menú que permita acceder a cada uno de los puntos por separado.

 '''

def muestra_menu():
    print("A)Recorrer la lista imprimiendo por consola el nombre de cada"
          "superhéroe de género M")
    print("B)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F")
    print("C)Recorrer la lista y determinar cuál es el superhéroe más alto de género M ")
    print("D)Recorrer la lista y determinar cuál es el superhéroe más alto de género F ")
    print("E)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M ")
    print("F)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F ")
    print("G)Recorrer la lista y determinar la altura promedio de los "
          "superhéroes de género M")
    print("H)Recorrer la lista y determinar la altura promedio de los  "
          "superhéroes de género F")
    print("I)Informar cual es el Nombre del superhéroe asociado a cada uno de"
          " los indicadores anteriores (ítems C a F)")
    print("J)Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("K)Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("L)Determinar cuántos superhéroes tienen cada tipo de inteligencia "
          " (En caso de no tener, Inicializarlo con ‘No Tiene’). ")
    
    
    print("M)Listar todos los superhéroes agrupados por color de ojos.")
    print("N)Listar todos los superhéroes agrupados por color de pelo.")
    print("O)Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("P) para salir.")


def recorre_imprime_nombre_segun_genero(lista_heroes: list, genero: str) -> None:

    for heroe in lista_heroes:
        if heroe["genero"] == genero:
            print(heroe["nombre"])


def heroe_segun_altura_genero(lista_heroes: list, genero: str, min_max: str, falg =0) -> None:
    heroe_aux = {}
    
        
    for heroe in lista_heroes:
        
        if not heroe_aux and heroe['genero'] == genero:
            heroe_aux = heroe
        if (heroe_aux and heroe['genero'] == genero):
            if ((min_max == 'Bajo' and float(heroe_aux['altura']) > float(
                heroe['altura']))
                or
                (min_max == 'Alto' and float(heroe_aux['altura']) < float(
                    heroe['altura']))):
                heroe_aux = heroe
    if falg == 0:            
        imprime_un_heroe(heroe_aux)
    else:
        print("\n\tNombre: {0}\n".format(heroe_aux['nombre']))


def calcular_promedio_altura_segun_genero(lista_heroes: list, genero: str) -> None:
    acumulador_personajes = 0
    contador = 0

    for heroe in lista_heroes:
        if genero == 'M' and heroe['genero'] == genero or genero == 'F' and heroe['genero'] == genero:
            acumulador_personajes += float(heroe["altura"])
            contador += 1

    print("\nEl promedio de altura del genero: {0} es {1:.2f}\n"
          .format(genero, acumulador_personajes / contador))

def imprime_un_heroe(heroe):
    print(f"\n\tNombre: {heroe['nombre']} - Altura: {heroe['altura']} mts.\n")


def contar_color_ojos(lista_heroes):
    color_ojos_dict = {}
    for heroe in lista_heroes:
        color_ojos = heroe['color_ojos']
        if color_ojos in color_ojos_dict:
            color_ojos_dict[color_ojos] += 1
        else:
            color_ojos_dict[color_ojos] = 1
    return color_ojos_dict



def contar_color_pelo(lista_heroes):
    color_pelo_dict = {}
    for heroe in lista_heroes:
        color_pelo = heroe['color_pelo']
        if color_pelo in color_pelo_dict:
            color_pelo_dict[color_pelo] += 1
        else:
            color_pelo_dict[color_pelo] = 1
    return color_pelo_dict


def contar_inteligencia(lista_heroes):
    dic_inteligencia = {}
    
    
    for heroe in lista_heroes:
        
        if 'inteligencia' in heroe and heroe['inteligencia'] != '':
            inteligencia = heroe['inteligencia']
        else:
            inteligencia = 'No Tiene'
        if inteligencia in dic_inteligencia:
            dic_inteligencia[inteligencia] += 1
        else:
            dic_inteligencia[inteligencia] = 1
       
    for clave in dic_inteligencia:
        valor = dic_inteligencia[clave]
        print("{0}: {1}".format(clave,valor))
        
       
    # for clave in dic_inteligencia.keys():
    #     valor = dic_inteligencia[clave]   
    #     print("\t: Inteligencia {0} , Cantidad: {1} ".format(clave, valor))
        
    # for clave, valor in dic_inteligencia.items():
    #     print(clave + ": " + str(valor))
        



def mostar_cantidad (cantida_color):
  # for elemento in lista_heroes:
    for clave in cantida_color.keys():
        valor = cantida_color[clave]   
        print("\tcolor: {0} , Cantidad: {1} ".format(clave, valor))




def agrupar_por_clave(lista_heroes, key):
    
    
    '''
    agrupa una lista de diccionarios de héroes según un atributo (clave"key") especificado.
    Parametros:
    lista_heroes -- lista de diccionarios de héroes
    key -- puede tomar la clave que necesite agrupar
    Retorna :
     diccionario -- con las listas  
    de diccionarios agrupadas según el valor del atributo especificado.
    
    
    
    Esta función toma una lista de diccionarios llamada "lista_heroes" 
    y una clave "key" como entrada. La función crea un nuevo diccionario 
    llamado "diccionario" donde los valores de la clave "key" de cada 
    diccionario de "lista_heroes" se utilizan como claves en el nuevo
    diccionario. Los valores del nuevo diccionario son listas de
    diccionarios que tienen la misma clave "key" y el mismo valor 
    de esa clave en "lista_heroes".

    Si la clave "key" no está presente en un diccionario de "lista_heroes"
    o su valor es una cadena vacía, se utiliza la cadena "No Tiene"
    
    como valor de esa clave. Luego, se comprueba si el valor de la clave
    "key" está presente en el nuevo diccionario. Si es así, el diccionario
    actual se agrega a la lista correspondiente en el diccionario.
    De lo contrario, se crea una nueva lista con ese diccionario como
    su único elemento y se agrega al nuevo diccionario bajo la clave correspondiente.

    Finalmente, la función devuelve el nuevo diccionario creado.
    
    '''
    
    

    if not lista_heroes and key not in lista_heroes[0]: 
        
        return {}
    
    diccionario = {}
    
    
    for heroe in lista_heroes:
        
        if key in heroe and heroe[key] != "":
            valor_key = heroe[key]
            
        else:
            valor_key = 'No Tiene'
            
            
        if  valor_key in diccionario:
            diccionario[valor_key].append(heroe)
            
        else:
            diccionario[valor_key] = [heroe]
            
    
    
    return diccionario




def imprimir_diccionario(diccionario):
    for clave in diccionario:
        print(clave + ":")
        for elemento in diccionario[clave]:
            print("\t {0}".format(elemento["nombre"]))
           
   
   
   
def listar_por_color_ojos(heroes):
    diccionario_ojos = agrupar_por_clave(heroes, 'color_ojos')
    imprimir_diccionario(diccionario_ojos)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def listar_por_color_pelo(heroes):
    
    diccionario_pelo = agrupar_por_clave(heroes, 'color_pelo')
    
    imprimir_diccionario(diccionario_pelo)
    
    
    
    
    
    
    
    
    
    
    
    

def listar_por_tipo_inteligencia(heroes):  
    diccionario_inteligencia = agrupar_por_clave(heroes, 'inteligencia')
    imprimir_diccionario(diccionario_inteligencia)
    

while True:
    muestra_menu()
    opcion = input("Ingrese una opcion: ")
    match opcion:
        case "A":
            recorre_imprime_nombre_segun_genero(lista_personajes, "M")
        case "B":
            recorre_imprime_nombre_segun_genero(lista_personajes, "F")
        case "C":
            heroe_segun_altura_genero(lista_personajes, "M", "Alto")
        case "D":
            heroe_segun_altura_genero(lista_personajes, "F", "Alto")
        case "E":
            heroe_segun_altura_genero(lista_personajes, "M", "Bajo")
        case "F":
            heroe_segun_altura_genero(lista_personajes, "F", "Bajo")
        case "G":
            calcular_promedio_altura_segun_genero(lista_personajes, 'M')
        case "H":
            calcular_promedio_altura_segun_genero(lista_personajes, 'F')
        case "I":
             heroe_segun_altura_genero(lista_personajes, "M", "Alto", 1)
             heroe_segun_altura_genero(lista_personajes, "F", "Bajo", 1)
          
        case "J":
            dict_cantidad_color_ojos = contar_color_ojos(lista_personajes)
            mostar_cantidad(dict_cantidad_color_ojos)
           
        case "K":
            mostar_cantidad(contar_color_pelo(lista_personajes))
        case "L":
            contar_inteligencia(lista_personajes)
        case "M":
            listar_por_color_ojos(lista_personajes)
        case "N":
            listar_por_color_pelo(lista_personajes)
        case "O":
            listar_por_tipo_inteligencia(lista_personajes)
        case "P":
            break
        case _:
            print('Error no disponible.')
