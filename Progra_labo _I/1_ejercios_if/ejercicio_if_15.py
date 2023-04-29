''''
Escribir un programa que le pida al usuario que ingrese un número entero positivo,
y luego imprima "El número es primo" si el número es primo, o 
"El número no es primo" si el número no es primo.
'''

numero = int(input("Ingrese un número entero positivo: "))

if numero <= 1:
    print("El número no es primo")
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("El número es primo")
    else:
        print("El número no es primo")
