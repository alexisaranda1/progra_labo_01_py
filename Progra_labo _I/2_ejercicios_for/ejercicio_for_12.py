#Dada una lista de números, imprimir la cantidad de números pares en la lista.

lista_numeros = [2, 3, 4, 5, 6, 7, 8, 9, 1, 20, 10, 12, 13, 14, 15, 10, 18, 16]

cantidad_pares = 0
for i in lista_numeros:
    if i % 2 == 0:
        cantidad_pares +=1
        
print("Cantidada de pares : ", cantidad_pares)
