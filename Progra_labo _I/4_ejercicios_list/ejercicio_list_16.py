#Crea dos listas con la misma cantidad de elementos y luego 
# crea una tercera lista que contenga los elementos de ambas listas intercalados. 
# Por ejemplo, si las dos listas son [1, 2, 3] y ["a", "b", "c"],
# la tercera lista debería ser [1, "a", 2, "b", 3, "c"].

lista_numeros = [1, 2, 3]

lista_letras =  ["a", "b", "c"]

lista_convinada = []

for i in range(len(lista_numeros)):
    lista_convinada.append(lista_numeros[i])
    lista_convinada.append(lista_letras[i])
    
print(lista_convinada)
    