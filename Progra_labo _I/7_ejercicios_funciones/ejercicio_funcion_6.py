#Crear una función que calcule el área de un triángulo. 
# Recibe dos parámetros (base y altura) y devuelve el área.


def calcular_area_triangulo(base: float, altura:float) -> float:   
    '''
    Calcula el área de un triangulo segun su base y altura.

    Parametros:
    base -- la base de un triangulo (float)
    altura -- la altura de un triangulo (float)
    
    Retorna:
    El área del triangulo (float) '''
    
    area = (base * altura) / 2
    
    return area


base_ingresada = float(input("Ingrese la base del triángulo: "))
altura_ingresada = float(input("Ingrese la altura del triángulo: "))
  
area = calcular_area_triangulo(base_ingresada, altura_ingresada)
print("El área del triángulo es: {0}".format(area))
