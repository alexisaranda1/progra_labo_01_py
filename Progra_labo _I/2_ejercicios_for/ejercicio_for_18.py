#Dada una lista de números, imprimir la suma de los números 
# en la lista que son mayores que el promedio de la lista.

lista_numeros = [2, 4, 5, 7, 9, 10]

suma  = 0

for numero in  lista_numeros:
   suma += numero
   
promedio = suma / len(lista_numeros)
print("promedio es : {0}".format(promedio))

suma_mayor = 0

for numero in  lista_numeros:
    if numero > promedio:
        print("numeros mayores al promedio: {0}".format(numero))
        suma_mayor += numero

print("La suma de numeros mayores al promedio : {0} ".format(suma_mayor))

