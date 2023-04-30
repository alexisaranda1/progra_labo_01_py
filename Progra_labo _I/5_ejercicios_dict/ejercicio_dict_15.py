
#Crea un diccionario que contenga el nombre y el sueldo de varios empleados.
# Luego, permite al usuario aumentar el sueldo de un empleado y actualizar
# el valor correspondiente en el diccionario.

empleados = {
    "Juan": 2500,
    "Pedro": 3000,
    "María": 2700,
    "Ana": 2800,
    "Luis": 3200
}

nombre = input("Ingrese el nombre del empleado que quiere aumentar el sueldo: ")
sueldo = int (input(" Ingrese el monto que quiere aumentar a {0} : ".format(nombre)))

empleados[nombre] = sueldo

print("Nombre : {0}, sueldo : {1}".format(nombre,empleados[nombre]))