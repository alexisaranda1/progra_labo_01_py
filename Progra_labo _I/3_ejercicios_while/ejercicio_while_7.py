#Dada una lista de números, imprimir todos los números que son mayores 
# que el promedio de la lista.

lista_numeros = [6, 5, 1, 9, 7]

suma_numero = 0
i = 0

while i < len(lista_numeros) :
    suma_numero += lista_numeros[i] 
    i += 1
    
promedio = suma_numero / i
print("\nEl promedio es :", promedio)

j = 0
print("\nNúmeros mayores al promedio: ")
while j < len(lista_numeros) :
    
    if lista_numeros[j] > promedio:
        print(lista_numeros[j])
    j +=1