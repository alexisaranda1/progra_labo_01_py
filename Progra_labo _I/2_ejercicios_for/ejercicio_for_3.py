#Dado un número entero n, imprimir la secuencia de números
# pares menores o iguales a n.

numero_entero = int (input("Ingrese un número entero : "))

for i in range(2,numero_entero+1,2) :
    print(i)
        
'''
for i in range(numero_entero+1) :
    if i % 2 == 0 :
    print(i)
'''      