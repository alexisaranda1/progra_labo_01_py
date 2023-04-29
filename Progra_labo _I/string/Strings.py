#1Escribir una función que reciba un string y devuelva 
# el mismo string todo en mayúsculas.

#Escribir una función que reciba un string y devuelva el mismo 
# string todo en minúsculas.


def muestra_menu():
    print("ejercicio: 1")
    print("ejercicio: 2")
    print("ejercicio: 3")
    print("ejercicio: 4")
    print("ejercicio: 5")
    print("ejercicio: 6")
    print("ejercicio: 7")
    print("ejercicio: 8")
    print("ejercicio: 9")
    print("ejercicio: 10")
    print("ejercicio: 11")
    print("ejercicio: 12")
    print("ejercicio: 13")
    print("ejercicio: 14")
    print("ejercicio: 15")
    print("ejercicio: 16")
    print("ejercicio: 17")
    print("ejercicio: 18")
    print("ejercicio: 19")
    print("ejercicio: 20")
    print("ejercicio: 21")
    print("opcion: 22 para salir.")
    
def cambiar_string_mayuscula(cadenada_caracteres:str)-> str:
    
    cadena_convertida_mayuscula = cadenada_caracteres.upper() 
    
    return   cadena_convertida_mayuscula

def cambiar_string_minuscula(cadenada_caracteres: str )-> str:
    
    cadena_convertida_minuscula = cadenada_caracteres.lower()
    
    return cadena_convertida_minuscula


def concatena_dos_cadenas_texto(primera_palabra: str, segunda_palabra: str) -> str:
    
    concatenado = primera_palabra + " " + segunda_palabra
    
    return concatenado

def calcuña_catidad_caracteres(texto: str) -> int :   
    
    cantidad_caracteres = len(texto)
  
    return cantidad_caracteres

def contar_cuantas_repite_caracter(texto: str, caracter_ingresado: str) -> int :
    
    contador = 0
    
    for caracter in texto:
        if caracter == caracter_ingresado:
            contador += 1
            
    return contador


def palabras_ese_caracter(texto : str, caracter_igresado : str) -> list:
   
    palabras = texto.split()
    
    palabras_caracteres = []
   
    for palabra in palabras:
      
        if caracter_igresado in palabra:
            palabras_caracteres.append(palabra)
    
    return palabras_caracteres

def elimina_espacios(texto: str):
     texto_sin_espacio = texto.replace(" ","")
     return texto_sin_espacio 
 
def nombre_apellido_sin_espacio(nombre: str , apellido : str) :
    
    nombre_sin_espacio = elimina_espacios(nombre)
    apellido_sin_espacio = elimina_espacios(apellido)
    
    nombre_primera_mayuscula = nombre_sin_espacio.capitalize()
    apellido_primera_mayuscula = apellido_sin_espacio.capitalize()
    
    
    
    dicionario_nombre_apellido = {"Nombre" : nombre_primera_mayuscula ,
                                  "Apellido" :apellido_primera_mayuscula }
    
    return dicionario_nombre_apellido


def unir_nombres(lista_nombres: list) :
    
    texto_nombres = '\n'. join(lista_nombres)
    
    return texto_nombres
def crear_mail(nombre:str, apelido:str):

    nombre_sin_espacios = elimina_espacios( nombre)
    apellido_sin_espacio = elimina_espacios( apelido)
    
    nombre_minuscula = cambiar_string_minuscula(nombre_sin_espacios)
    apelido_minuscula =cambiar_string_minuscula(apellido_sin_espacio)
    
    email_crado = f"{nombre_minuscula[0]}.{apelido_minuscula}@utn-fra.com.ar" 
   
    return email_crado

    
while True:
    muestra_menu()
    opcion_str = input("Ingrese una opcion: ")
    opcion = int(opcion_str)
    match opcion:
        case 1:
            #Escribir una función que reciba un string y devuelva el
            # mismo string todo en mayúsculas.
            cadena_ingresada = input("ingrese una cadena de texto: ")
            resultado = cambiar_string_mayuscula(cadena_ingresada)
            print(resultado)
            
        case 2:
            #Escribir una función que reciba un string y 
            # devuelva el mismo string todo en minúsculas.
            cadena_ingresada = input("ingrese una cadena de texto: ")
            canda_minuscula = cambiar_string_minuscula(cadena_ingresada)
            print(canda_minuscula)
            
        case 3:
            #Escribir una función que tome dos strings y devuelva 
            # un nuevo string que contenga ambos strings concatenados,
            # separados por un espacio.
            cadena_ingresada_uno = input("ingrese una cadena de texto: ")
            cadena_ingresada_dos = input("ingrese una cadena de texto: ")
            cadena_concatenada = concatena_dos_cadenas_texto (cadena_ingresada_uno, cadena_ingresada_dos)
            print(cadena_concatenada)
            
        case 4:
            #Escribir una función que tome un
            # string y devuelva el número de caracteres que tiene el string.
            cadena_ingresada_uno = input("ingrese una cadena de texto: ")
            print(calcuña_catidad_caracteres(cadena_ingresada_uno))
            
        case 5:
            #Escribir una función que tome un string y un carácter y devuelva 
            # el número de veces que aparece ese carácter en el string
            cadena_ingresada = input("ingrese una cadena de texto: ")
            caracter = input("ingrese un caracter para ver si se repite: ")
            cantida = contar_cuantas_repite_caracter(cadena_ingresada,caracter)
            print(cantida)
            
        case 6:
            #Escribir una función que tome un string y un carácter y devuelva una 
            # lista con todas las palabras en el string que contienen ese carácter.
            cadena_ingresada = input("ingrese una cadena de texto: ")
            caracter = input("ingrese un caracter para ver si se repite: ")
            lista_palabra = palabras_ese_caracter(cadena_ingresada,caracter)
            print(lista_palabra)
        case 7:
            #Escribir una función que tome un string
            # y devuelva el mismo string con los espacios eliminados
            cadena_ingresada = input("ingrese una cadena de texto: ")
            cadena_sin_espacio = elimina_espacios(cadena_ingresada)
            print(cadena_sin_espacio)
        case 8:
            #Escribir una función que reciba dos string (nombre y apellido)
            # y devuelva un diccionario con el nombre y apellido, eliminando 
            # los espacios del comienzo y 
            # el final y colocando la primer letra en mayúscula
            nombre = input("ingrese su nombre : ")
            apellido = input("ingrese su apellido : ")
            
            dicionario = nombre_apellido_sin_espacio(nombre, apellido)
            
            print(dicionario["Nombre"], dicionario["Apellido"])
        
        case 9:
            #Escribir una función que tome una lista de nombres y 
            # los una en una sola cadena separada por un salto
            # de línea, por ejemplo: ["Juan", "María", "Pedro"]
            # -> "Juan\nMaría\nPedro".
            lista_nombres = ["Juan", "María", "Pedro", "Ana", "Pablo"]
            texto_nombres = unir_nombres(lista_nombres)
            print(texto_nombres)
            
        case 10:
            #Escribir una función que tome un nombre y un
            # apellido y devuelva un email en formato
            # "inicial_nombre.apellido@utn-fra.com.ar"
            
            nombre = input("ingrese su nombre : ")
            apellido = input("ingrese su apellido : ")
            mail = crear_mail(nombre , apellido)
            print(mail)
          
        case 11:
          pass
        case 12:
            pass
        case 13:
            pass
        case 14:
          pass
        case 15:
            break
        case 16:
           pass
        case 17:
          pass
        case 18:
            pass
        case 19:
            pass
        case 20:
          pass
        case 21:
            break
        case 22:
            break
        case _:
                print('Error no disponible.')