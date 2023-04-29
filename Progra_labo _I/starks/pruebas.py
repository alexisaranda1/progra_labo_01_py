from data_stark import lista_personajes


def contar_inteligencia(lista_heroes):
    dic_inteligencia = {}

    for heroe in lista_heroes:

        if 'inteligencia' in heroe and heroe['inteligencia'] != '':
            inteligencia = heroe['inteligencia']
        else:
            inteligencia = 'No Tiene'
        if inteligencia in dic_inteligencia:
            dic_inteligencia[inteligencia] += 1
        else:
            dic_inteligencia[inteligencia] = 1

    for clave in dic_inteligencia:
        valor = dic_inteligencia[clave]
        print("{0}: {1}".format(clave,valor))
        
    # for clave in dic_inteligencia.keys():
    #     valor = dic_inteligencia[clave]   
    #     print("\t: Inteligencia {0} , Cantidad: {1} ".format(clave, valor))
        
    # for clave, valor in dic_inteligencia.items():
    #     print(clave + ": " + str(valor))



contar_inteligencia(lista_personajes)
