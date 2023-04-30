
#Crea un diccionario que represente una lista de las compras.
# Cada clave del diccionario debe ser el nombre de un 
# producto y cada valor debe ser su cantidad. 

# Pedir al usuario que ingrese el nombre del producto e imprimir la cantidad

lista_compras = {
    "Leche": 2,
    "Huevos": 12,
    "Pan": 1,
    "Manzanas": 6,
    "Carne": 1
}

nombre = input("ingrese el nombre de un producto: ")

print("Nombre del producto : {0} y la cantidad es : {1} ".format(nombre,lista_compras[nombre]))