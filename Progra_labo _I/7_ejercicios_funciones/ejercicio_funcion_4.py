# Crear una función que calcule el promedio de edad de un grupo de personas.
# Recibe una lista de edades y devuelve el promedio.

def promedio_edad(edades: int) -> int:
    """
    Calcula el promedio de edad de un grupo de personas.

    parametros:
    edades -- una lista de edades 

    Retorna:
    El promedio de edad como un número de punto flotante.
    """
    suma = 0
    for edad in edades:
        suma += edad
    promedio = suma / len(edades)
    return promedio

edades = [13,32,4,55,19]

print("el promedio de edades es : {0}".format(promedio_edad(edades)))