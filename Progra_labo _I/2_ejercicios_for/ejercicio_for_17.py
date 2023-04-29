#Dado un número entero n, imprimir la secuencia de números de Harshad
# menores o iguales a n.

numero = int(input("ingrese un número entero: "))

for i in range(1, numero+1):
    suma_digitos = 0
    for digito in str(i):
        suma_digitos += int(digito)
    if i % suma_digitos == 0:
        print(i)

