#crea dos listas de 10 números enteros cada una 
# y realiza una multiplicación de los elementos
# con el mismo índice en ambas listas.

lista_numeros =[12,23,3,4,5,6,7,8,9,2 ]
lista_numeros_segundo = [2,3,8,4,6,9,7,5,2,8]
multiple = 0
for i in range(10):
    multiple += lista_numeros[i] * lista_numeros_segundo[i] 
print("la miltiplicacion es : {}".format(multiple))

