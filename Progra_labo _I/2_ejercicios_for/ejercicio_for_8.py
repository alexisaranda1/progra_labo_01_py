#Dado un número entero n, imprimir la suma de los números pares menores o iguales a n.

numero_ingresado = int ( input("ingrese un números : "))
suma_pares = 0

for i in range(2,numero_ingresado+1,2) :
    suma_pares += i
    
print("La suma del os números pares es : ", suma_pares)
