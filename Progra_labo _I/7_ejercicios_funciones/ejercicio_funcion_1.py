#Crear una función que convierta grados Celsius a grados Fahrenheit. 
# Recibe un parámetro (grados Celsius) 
# y devuelve el resultado en grados Fahrenheit.

def celsius_a_fahrenheit(grado_celsius: float) -> float:
    ''' 
    convierte de celsius a fahrenheit.

    Parametro:
    grado celsius -- la temperatura en grado celsius
    
    Retorna:
    La temperatura en grados fahrenheit
    '''
    fahrenheit = grado_celsius * 1.8 + 32
    return fahrenheit


celsius_string = input("Ingrese la temperatura en grados Celsius: ")
celsius = float(celsius_string)
grado_fahrenheit = celsius_a_fahrenheit(celsius)

print("El resultado en grados Fahrenheit: {0}".format(grado_fahrenheit))
