#Dada una lista de números, imprimir todos los números que son múltiplos de 3.
numeros = [1, 5, 12, 23, 37, 42, 56, 68, 71, 81]

i = 0

while i < len(numeros):
    if numeros[i] % 3 == 0:
        print("{0} es multiplo de 3 ".format(numeros[i]), end=' ')
    i += 1 