#Dada una lista de números, imprimir el número más grande de la lista.

lista_enteros = [1,2,50,5]
numero_max = 0
for numero in lista_enteros:
    if (numero > numero_max) :
       numero_max = numero
       
print("numero", numero_max)

