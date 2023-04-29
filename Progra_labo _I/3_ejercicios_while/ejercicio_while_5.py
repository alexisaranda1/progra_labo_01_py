
#Dado un número entero n, imprimir si el número es primo o no.

numero_entero = int(input("Ingrese un número entero: "))
es_primo = True
i = 2

while i < numero_entero:
    
    if numero_entero % i == 0:
        es_primo = False
        break
    i += 1
if es_primo:
    print("El número es primo")
else:
    print("El número no es primo")