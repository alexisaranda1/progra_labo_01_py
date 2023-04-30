#A partir de la lista: [1,80,5,0,15,-5,1,79] 
# determinar, el mayor, el menor, el promedio 
# y la suma total de todos los elementos}

lista_numeros =  [1,80,5,0,15,-5,1,79] 

numero_max = lista_numeros[0]
numero_min = lista_numeros[0]
suma_numeros = 0
cantidad = len(lista_numeros)

i = 0

while i < len(lista_numeros):
    
    if lista_numeros[i] > numero_max:
        numero_max = lista_numeros[i]
        
    if lista_numeros[i] < numero_min:
        numero_min = lista_numeros[i]

    suma_numeros += lista_numeros[i]
    
    i +=1
    
print("El numero mayor es : {0}".format(numero_max))
print("El numero mas chico es : {0}".format(numero_min))
print("La suma de los numero es : {0}".format(suma_numeros))    
print("El promedio es : {0}".format(suma_numeros/cantidad))
    