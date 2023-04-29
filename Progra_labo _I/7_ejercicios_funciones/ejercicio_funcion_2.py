#Crear una función que calcule el área de un círculo. 
# Recibe un parámetro (radio) y devuelve el área del círculo.


def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo segun su radio.

    Parametros:
    radio -- el radio de un círculo 
    
    Retorna:
    El área del círculo 
    """
    area = 3.1415 * radio ** 2
    return area


radio_string = input("ingrese el radio del triangulo: ")
radio_float = float(radio_string)

area = calcular_area_circulo(radio_float)

print("el área del circulo es : {0}".format(area))

