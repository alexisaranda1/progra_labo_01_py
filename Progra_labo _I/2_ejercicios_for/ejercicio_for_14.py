# Dado un número entero n, imprimir la secuencia de números perfectos
# menores o iguales a n.

numero = int(input("Ingrese un número entero: "))
print("Los números perfectos menores o iguales a", numero, "son:")

for indice in range(1, numero+1):
    suma = 0
    for i in range(1, indice):
        if indice % i == 0:
            suma += i
    if suma == indice:
        print(indice)
