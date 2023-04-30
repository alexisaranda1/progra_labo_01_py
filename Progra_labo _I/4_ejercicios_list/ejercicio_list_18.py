# Solicitar al usuario números enteros hasta que ingrese el 0.
# Almacenar los números en una lista y luego imprimir
# el mayor (sin utilizar la función max())

numero_ingresado = None
lista_numeros = []
while numero_ingresado != 0:
    numero_ingresado = int(input("ingrese un numero : "))
    if numero_ingresado != 0:
        lista_numeros.append(numero_ingresado)


mayor = lista_numeros[0]

for numero in lista_numeros:
    if numero > mayor:
        mayor = numero

print(mayor)
