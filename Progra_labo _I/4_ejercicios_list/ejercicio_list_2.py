#Crea una lista con 5 números enteros. 
# Luego solicita un nuevo número y reemplaza el tercer
# elemento de la lista por el número ingresado.
# Finalmente imprime todos los números

list_numeros = [2, 3, 4, 5, 6]
print("La lista sin modificar es : {0}".format(list_numeros))
numero = int(input("Ingrese un numero : "))
list_numeros[2] = numero

print("La lista modificada es : {0}".format(list_numeros))
