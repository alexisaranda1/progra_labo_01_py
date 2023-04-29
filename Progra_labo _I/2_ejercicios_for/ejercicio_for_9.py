#Dada una lista de números, imprimir la cantidad de números negativos en la lista.
lista_numeros= [-5, 6, 10, 5, 9]
cantidad_negativos = 0

for i in lista_numeros:
        if i < 0:
            cantidad_negativos += 1
if cantidad_negativos != 0:
    print("Catidad de numeros de nagaticos : ", cantidad_negativos)
else :
    print("No hay numeros negativos..")