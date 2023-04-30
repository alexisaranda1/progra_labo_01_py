#Crear un programa que solicite al usuario ingresar 
# precio unitario y cantidad de 5 productos. Almacenar cada
# valor en dos listas distintas. Luego imprimir 
# el precio total de cada artículo.

precios = []
cantidades = []


for i in range(5):
    i +1
    precio = float(input(f"Ingrese el precio unitario del producto {i+1}: "))
    cantidad = int(input(f"Ingrese la cantidad del producto {i+1}: "))
    

    precios.append(precio)
    cantidades.append(cantidad)


for i in range(5):
    precio_total = precios[i] * cantidades[i]
    print("El precio total del artículo {0} es: {1}".format(i+1,precio_total))
