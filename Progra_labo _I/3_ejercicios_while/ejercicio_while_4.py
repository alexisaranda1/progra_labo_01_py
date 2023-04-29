# Dada una lista de números, imprimir la suma de todos los elementos de la lista.
 
lista_enteros = [5, 6, 4, 9, 2]

i = 0
suma = 0

while i < len(lista_enteros):
    suma += lista_enteros[i]
    i += 1

print("la suma de todos los elementos de la lista es : ", suma)