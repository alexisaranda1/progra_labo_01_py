#Dado un número entero n, imprimir la suma de
# todos los números pares menores o iguales a n.

numero_entero = int(input("Ingrese un número entero: "))
i = 0
suma_numero = 0
while i < numero_entero:
    i += 1
    if i % 2 == 0 :
        suma_numero += i
print("La suma de los numeros pares es : ",suma_numero)