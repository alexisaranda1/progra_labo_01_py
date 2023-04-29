#Dada una cadena de texto, imprimir la cadena al revés.

cadena_original = "Cómo estas?"
i = len(cadena_original) - 1
cadena_al_reves = ""

while i >= 0:
    cadena_al_reves += cadena_original[i]
    i -= 1

print(cadena_al_reves)
