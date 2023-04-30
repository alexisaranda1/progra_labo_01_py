#Crear un programa que solicite al usuario ingresar: nombre del 
# producto, cantidad y precio unitario. Guardar los datos en 3
# listas distintas. Solicitar productos hasta que 
# el nombre del producto sea ‘xxx’. Luego imprimir 
# la lista de artículos con el siguiente formato:
productos_nombres = []
productos_cantidades = []
productos_precios = []

#nombre_articulo	cantidad	$ precio_unitario 	$ total
#	Ejemplo:

#	alfajor capitan del espacio		6	$ 150		$ 900



producto_nombre = ""
i = 0


while True:
    
    
    producto_nombre = input (f"ingrese el nombre del producto {i+1} : " )
    if producto_nombre == "xxx":
        break
    producto_cantidad = int(input (f"ingrese la cantidad del producto {i+1} : " ))
    produto_precio = float (input(f"ingres el precio del producto {i+1} : "))
    
    productos_nombres.append(producto_nombre)
    productos_cantidades.append(producto_cantidad)
    productos_precios.append(produto_precio)
    i += 1
    
# Imprimir los datos de los productos en una tabla
print("\tnombre_articulo\tcantidad\t$ precio_unitario\t$ total")
for i in range(len(productos_nombres)):
    precio_total = productos_cantidades[i] * productos_precios[i]
    print("\t{0}\t\t{1}\t\t{2}\t\t\t{3}".format(productos_nombres[i], productos_cantidades[i], productos_precios[i], precio_total))