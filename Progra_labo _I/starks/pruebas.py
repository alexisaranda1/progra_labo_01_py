import re

# cadena = "esto es una cadena  de una larga lista"
# buscar = "una"
#                 #texto a buscar , variable en la que se busca
# #print(re.search("una", cadena)) # devuelvee un objeto si ecuentra el texto y None si no encuentra

# texto_encontrado = re.search(buscar, cadena)

# print(texto_encontrado.start()) # encuentra comienzo de ese texto
# print(texto_encontrado.end()) #encuntra dodne finalisa el texo encontradp
# print(texto_encontrado.span()) # devulve una tupla el caracter dondeempieza y termina

# # if re.search(buscar, cadena):
# #     print("se encontro el texto")
# # else:
# #     print("no se encontro")

# palabras = re.findall(buscar, cadena)# de vuelva una lista con la plalabra encontrada si aparece 2 veces va salir 2 veces
# print(palabras)
# cantidad = len(re.findall(buscar, cadena)) # cantidad de veces que aparece una palabra
# print(cantidad)

# lista_nombre_apellido = ['ana xxx',
#     'pablo vidal ', 'pepe Argento', 'pepito xxx' , 'ana argento']

# for nombre in  lista_nombre_apellido:
#             #busca la palabra que comienza por ana con ^
#     if re.findall('^ana',nombre):
#         print(nombre)
#                 #busca la palabra que finaliza con xxx con $ sabe que esl qeu qeu finaliza
#     if re.findall('xxx$',nombre):
#         print(nombre)


texto = 'uno 1 dos 2 tres 3 cuatro'
print(re.split(' ', texto))
#['uno', '1', 'dos', '2', 'tres', '3', 'cuatro']
print(re.split('[0-9]+', texto))
#['uno ', ' dos ', ' tres ', ' cuatro']
print(re.split('[a-z ]+', texto))
#['', '1', '2', '3', '']

