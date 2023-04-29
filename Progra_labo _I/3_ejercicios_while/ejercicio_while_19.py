#Dada una lista de números, imprimir todos los números que son mayores 
# que el número anterior en la lista.

numeros = [3, 5, 2, 8, 4, 10, 7]
anterior = numeros[0]
i = 1

while i < len(numeros):
    if numeros[i] > anterior:
        print(numeros[i])
    anterior = numeros[i]
    i += 1
