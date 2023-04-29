#Dada una lista de números, imprimir la cantidad de
# números impares en la lista.

lista_numeros = [2, 4, 5, 7, 9, 10]

contador = 0

for numero in  lista_numeros:
    if numero % 2 != 0:
        contador  += 1
        
print("Cantidad de numeros impares  : {0}".format(contador))



