#Dado un número entero n, imprimir la secuencia de números primos menores 
# o iguales a n.


numero = int(input("Ingrese un número entero: "))

for i in range(2, numero+1):
    """_summary_
    """    es_primo = True
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        print(i, end=" ")#se imprimirá en la misma línea separdo por un " " y no Por \n
