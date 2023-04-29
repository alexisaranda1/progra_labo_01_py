# Dado un número entero n, imprimir todos los números perfectos menores 
# o iguales a n. Los números perfectos son aquellos números enteros
# positivos que son iguales a la suma de sus divisores propios 
# (excluyendo al propio número). En otras palabras, 
# si sumamos todos los divisores propios de un número
# (excluyendo el número en sí mismo) y el resultado 
# es igual al número, entonces ese número se considera un número perfecto.

# Por ejemplo, el primer número perfecto es 6, ya que sus divisores
# propios son 1, 2 y 3, y 1 + 2 + 3 = 6. 
# Otros ejemplos de números perfectos son 28, 496 y 8128.
# Actualmente se conocen más de 50 números perfectos, 
# y se cree que existen infinitos números perfectos,
# aunque no se ha podido demostrar matemáticamente esta afirmación.

numero = int(input("Ingrese un número entero: "))
i = 1

while i <= numero:
    acumulador_divisores = 0
    j = 1
    
    while j < i:
        if i % j == 0:
            acumulador_divisores += j
        j += 1
        
    if acumulador_divisores == i:
        print(i, "es un número perfecto")
        
    i += 1
