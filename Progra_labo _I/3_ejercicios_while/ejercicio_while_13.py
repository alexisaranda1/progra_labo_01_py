#Dada una lista de números, imprimir la cantidad de números negativos en la lista.
numeros = [-10, 5, -2, 0, 8, -4, 7, -1, -9, 3]

i = 0
acumulador_negativos = 0

while i < len (numeros):
    if numeros[i] < 0:
       acumulador_negativos += 1 
       
    i += 1
print("la cantidad de numeros negativos es : {0}".format(acumulador_negativos))