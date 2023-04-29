#Dado un número entero n, imprimir la secuencia de números 
# impares menores o iguales a n.

numero_entero = int (input("Ingrese un número entero : "))

for i in range(1,numero_entero+1,2) :
    print(i)