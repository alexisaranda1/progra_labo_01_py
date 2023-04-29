#Dado un número entero n, imprimir todos los números primos menores o iguales a n.

numero = int(input("Ingrese un número entero: "))

i = 2
while i <= numero:
    es_primo = True
    j = 2
    while j < i:
        if i % j == 0:
            es_primo = False
            break
        j += 1
        
    if es_primo:
         print(i, end=', ')
       
    i += 1


