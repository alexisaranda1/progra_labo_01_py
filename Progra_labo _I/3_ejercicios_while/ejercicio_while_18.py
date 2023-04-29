#Dado un número entero n, imprimir la suma de todos los números que son múltiplos
# de 5 menores o iguales a n.

numero = int (  input("ingrese un numero entero : ") )
i = 1
acumulador = 0
while i < numero:
    if i % 5 == 0:
        print(i)
        acumulador += i
    i += 1 
print("la suma de los numeros multiplos de 5 es : {0}".format(acumulador))