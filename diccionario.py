def run():
    mi_diccionario = { #las llaves en python sirven para definir diccionarios
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }
    # print(mi_diccionario["llave1"]) #de esta manera podemos accedar al contenido que queramos conocer
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])
    población_paises = {
	    'Argentina': 44_938_712,
	    'Brasil': 210_147_125,
	    'Colombia': 50_372_424
    }
        #print(población_paises["Argentina"])
    # for pais in población_paises.keys(): # .keys es un metodo del diccionario que me devuelve las llaves.  en este ciclo for lo que estamos haciendo es que en cada vuelta me duvuelva el valor  de las llaves
    #     print(pais)
    # for pais in población_paises.values():# el metodo values lo que hace es devolver los valores del diccionario
    #     print(pais)
    for pais, poblacion in población_paises.items(): #el metodo items me devuelve los dos valores, la llave y el valor de esa llave en el diccionario
        print(pais + " tiene " + str(poblacion) + " habitantes")



if __name__ == "__main__":
    run()


#DICCIONARIOS

# Diccionarios: Son una estructura de datos mutable las cuales almacenan diferentes tipos de valores sin darle importancia a su orden. Identifican a cada elemento por una clave (Key). Se escriben entre {}.

# Operaciones:

# .keys() —> Retorna la clave de nuestro elemento

# .values()—> Retorna una lista de elementos (valores del diccionario)

# .items() —> Devuelve lista de tuplas (primero la clave y luego el valor)

# .clear() —> Elimina todos los items del diccionario

# .pop(“n”) —> Elimina el elemento ingresado