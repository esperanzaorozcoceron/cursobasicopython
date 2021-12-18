def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuantos pesos" + tipo_pesos + "tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)  
    dolares = str(dolares)
    print("tienes $" + dolares + "dolares")

menu = """  
Bienvenido al conversor de moneda 

1- pesos Colombianos
2- pesos Argentinos
3- pesos Mexicanos

Elige una opcion: """  #las tres comillas en python me permiten escribir texto en la que podemos poner una cadena de caracteres de varias lineas

opcion = int(input(menu))  #con esto le mostramos el mensaje al usuario  a lo que escriba el usuario lo vamos a almacenar con input y a eso lo voy a poner dentro de mi variable opcion
if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Ingresa una opcion correcta")


# if opcion == 1:
#     pesos = input("¿cuantos pesos colombianos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 3875
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)  #con el comando round lo que hago es redondear la variable que quiero y especifico la cantidad que quiero que redondee
#     dolares = str(dolares)
#     print("tienes $" + dolares + "dolares") #todo esto que tenemos aqui corresponde a un bloque de codigo
# elif opcion == 2:
#     pesos = input("¿cuantos pesos argentinos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 65
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)  
#     dolares = str(dolares)
#     print("tienes $" + dolares + "dolares")
# elif opcion == 3:
#     pesos = input("¿cuantos pesos mexicanos tienes?: ")
#     pesos = float(pesos)
#     valor_dolar = 24
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)  
#     dolares = str(dolares)
#     print("tienes $" + dolares + "dolares")
# else:
#     print("ingresa una opcion correcta")


