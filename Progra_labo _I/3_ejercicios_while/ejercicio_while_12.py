#Dado un número entero n, imprimir la suma de todos
# los números impares menores o iguales a n.

numero = int( input("ingrese un numero : "))

i = 0
acumulador = 0

while i < numero:
    if i %2 !=0:
        acumulador += i
        print("impar: {}".format(i))
    i += 1
    
print("la suma de los impares es : {}".format(acumulador))