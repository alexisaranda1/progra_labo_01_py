#Dado un número entero n, imprimir la suma de los números 
# impares menores o iguales a n.

numero_entero = int (input("Ingrese un número entero : "))
suma_impares =0

for i in range(1,numero_entero+1,2) :
    suma_impares += i
    
print("La suma de los impares es : ", suma_impares)
