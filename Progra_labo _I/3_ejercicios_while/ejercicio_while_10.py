#Dada una lista de números, imprimir la cantidad de números pares en la lista.

numeros = [1, 5, 10, 23, 37, 42, 56, 68, 71, 81]

contador = 0
i = 0

while i < len(numeros) :
    if numeros[i] %2 == 0:
        print("numeros pares_: {0}".format(numeros[i]))
        contador += 1
    i += 1

print("catidad de numeros pares es: {0}".format(contador))
    