#Crea dos listas de números y encuentra los 
# elementos que se encuentran en ambas listas.

lista1 = [2, 5, 8, 10, 15]
lista2 = [3, 7, 10, 15, 20, 25]

elementos_comunes = []

for elemento in lista1:
    if elemento in lista2:
        elementos_comunes.append(elemento)

print("Los elementos comunes en ambas listas son:", elementos_comunes)
