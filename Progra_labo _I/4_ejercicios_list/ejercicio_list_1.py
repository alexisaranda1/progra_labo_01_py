#Crea una lista con los números del 1 al 10 e imprime solo los números impares.
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista_numeros:
    if numero % 2 != 0:
        print("numero: {0} ".format(numero))