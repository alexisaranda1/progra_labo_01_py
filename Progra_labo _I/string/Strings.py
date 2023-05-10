#1Escribir una función que reciba un string y devuelva 
# el mismo string todo en mayúsculas.

#Escribir una función que reciba un string y devuelva el mismo 
# string todo en minúsculas.


import os
def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')


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
    
    email_crado = f"{nombre_minuscula[0]}{apelido_minuscula[0]}_{nombre_minuscula}.{apelido_minuscula}@utn-fra.com.ar" 
   
    return email_crado



def concatenar_palabras(lista_palabras):
    if len(lista_palabras) == 0:
        return ""
    elif len(lista_palabras) == 1:
        return lista_palabras[0]
    else: 
        # une todas las palabras con (,) excepto la última
        palabras_concantenada = ', '.join(lista_palabras[:-1]) 
        # agrega la última palabra a la cadena
        palabras_concantenada += ' y ' + lista_palabras[-1]  
        
        return palabras_concantenada
    


def verifica_tarjeta(numero_tarjeta):
    # Verificar si el número de tarjeta contiene solo caracteres numéricos
    if not numero_tarjeta.isnumeric():
        return "Número de tarjeta inválido"
    
    # Obtener los últimos cuatro dígitos
    ultimos_cuatro_digitos = numero_tarjeta[12:]
    
    # Obtener la longitud de la cadena de número de tarjeta
    longitud = len(numero_tarjeta)
    
    # Obtener el número de caracteres que se deben ocultar
    num_caracteres_ocultos = 12
    
    # Crear una cadena de asteriscos de la misma longitud que el número de caracteres que se deben ocultar
    asteriscos = '*' * num_caracteres_ocultos
    
    # Combinar los asteriscos y los últimos cuatro dígitos para formar la cadena final
 
    resultado = "{0} {1}".format(asteriscos,ultimos_cuatro_digitos)
    
    return resultado
def rellenar_bits(numero_binario: str) -> str :
    
    numero = numero_binario.zfill(8)
    return numero

def filtra_usuario(correo):
     filtro = correo.split("@")
     
     usuario = filtro[0]
     
     return usuario
 
def filtrar_domino(dominio):
    filtrado = dominio.split(".")
    dominio_nombre = filtrado[1]
    return dominio_nombre

def elimina_numero_simbolos(texto):
    texto_limpio = ""
  
    for caracter in texto:
        if caracter.isalpha() or caracter == " ":
            texto_limpio += caracter
    
    return texto_limpio

def convierte_acronimo(texto):
    acronimo = ""
    palabras = texto.split()
    
    for palabra in palabras:
        acronimo += palabra[0]
        
    acronimo_mayusucla = acronimo.upper()
    return acronimo_mayusucla
def reemplaza_mayuscula_minuscula(cadena):
    cadena_convertida = ""
    for caracter in cadena:
        
        if caracter.isupper():
            cadena_convertida += caracter.lower()
        elif caracter.islower():
            cadena_convertida += caracter.upper()
    return cadena_convertida

def calcula_cantida_numeros_cadena(cadena_caracteres):
    contador_numeros = 0
    for caracter in cadena_caracteres:
        if caracter.isnumeric():
            contador_numeros += 1
    return contador_numeros
def unir_correos(lista_correos):
    correos_unidos = ";".join(lista_correos)
    return correos_unidos

def contar_palabras(texto):
    palabras = texto.split()
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = texto.count(palabra)
    return diccionario







#main
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
            #Escribir una función que tome una lista de palabras
            # y devuelva un string que contenga todas las palabras 
            # concatenadas con comas y "y" antes de la última palabra. 
            # Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], 
            # el string resultante debería ser "manzanas, naranjas y bananas"..
            lista = ["manzanas", "naranjas", "bananas"]
            resultado = concatenar_palabras(lista)
            print(resultado) # Salida: "manzanas, naranjas y bananas"
                   
        case 12:
            #Escribir una función que tome un número de tarjeta de crédito
            # como input, verificar que todos los caracteres sean
            # numéricos y devolver los últimos cuatro dígitos y los 
            # primeros dígitos como asteriscos,
            # por ejemplo: "**** **** **** 1234". 
            
            numero_tarjeta = input("Ingrese el  número de la tarjeta de crédito: ")
            
            numero_tarjeta_verificada = verifica_tarjeta(numero_tarjeta)
            print(numero_tarjeta_verificada)
            pass
        case 13:
            #Escribir una función que tome un correo electrónico y elimine 
            # cualquier carácter después del símbolo @, por 
            # ejemplo: "usuario@gmail.com" -> "usuario
            correo = "usuario@gmail.com"
            usuario = filtra_usuario(correo)
            print(usuario)
            
    

        case 14:
            #Escribir una función que tome una URL y devuelva solo el nombre 
            # de dominio, por ejemplo: "https://www.ejemplo.com.ar/pagina1"
            # -> "ejemplo"..
            dominio = "https://www.ejemplo.com.ar/pagina1"
            
            dominio_nombre = filtrar_domino(dominio)
            
            print(dominio_nombre)
    
        case 15:
            #Escribir una función que tome una cadena 
            # de texto y devuelva solo los caracteres alfabéticos, 
            # eliminando cualquier número o símbolo 
            # (sólo son válidos letras y espacios),
            # por ejemplo: "H0l4, m4nd0!" -> "Hl mnd”
            texto ="H0l4, m4nd0!"
            
            texto_limpio = elimina_numero_simbolos(texto)
            print(texto_limpio)
         
        case 16:
            #Escribir una función que tome una cadena de texto
            # y la convierta en un acrónimo, tomando la primera
            # letra de cada palabra, por ejemplo: "Universidad 
            # Tecnológica Nacional Facultad Regional Avellaneda"
            # -> "UTNFRA”.
            acronimo = convierte_acronimo("Universidad Tecnológica Nacional Facultad Regional Avellaneda")
            print(acronimo)
    
        case 17:
            #Escribir una función que tome un número binario y lo convierta
            #en una cadena de 8 bits, rellenando con ceros a la izquierda 
            # si es necesario, por ejemplo: "101" -> "00000101".
            numeros_binarios = input("Ingres numero binarios: ")
            numeros_binarios_bits = rellenar_bits(numeros_binarios)
            print(numeros_binarios_bits)
        case 18:
            #Escribir una función que tome una cadena de caracteres y 
            # reemplace todas las letras mayúsculas por letras minúsculas 
            # y todas las letras minúsculas por letras mayúsculas,
            # por ejemplo: "HoLa" -> "hOlA"
            cadena = "HoLa"
            cadena_covertida = reemplaza_mayuscula_minuscula(cadena)
            print(cadena_covertida)
            pass
        case 19:
            #scribir una función que tome una cadena de caracteres y cuente
            # la cantidad de dígitos que contiene, por ejemplo: 
            # "1234 Hola Mundo" -> contiene 4 dígitos.
            cadena_caracteres = "1278934 Hola Mundo"
            caracteres_contados = calcula_cantida_numeros_cadena(cadena_caracteres)
            print("contiene {0} dígitos".format(caracteres_contados))
        case 20:
          #Escribir una función que tome una lista de direcciones de correo 
          # electrónico y las una en una sola cadena separada por punto 
          # y coma, 
          # por ejemplo: ["juan@gmail.com", "maria@hotmail.com"]
          # -> "juan@gmail.com;maria@hotmail.com".
          lista_correos =["juan@gmail.com", "maria@hotmail.com"]
          coreos_unidos = unir_correos(lista_correos)
          print(coreos_unidos)
        case 21:
            #Crear una función que reciba como parámetro un string y devuelva un diccionario 
            # donde cada clave es una palabra y cada valor es un entero que indica cuántas 
            # veces aparece esa palabra dentro del string.
            texto = "Este es un ejemplo de texto. Este texto tiene varias palabras, algunas de ellas se repiten."
            cantidad_aparece = contar_palabras(texto)
            print(cantidad_aparece)

        case 22:

            
            break
        case _:
                print('Error no disponible.')
    clear_console()