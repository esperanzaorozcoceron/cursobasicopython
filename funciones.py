# def imprimir_mensaje(): #con def empezamos a definir una funcion 
#     print("mensaje especial: ")
#     print("estoy a prendiend a usar funciones")
# #una funcion es el lugar donde yo puedo escribir codigo que voy a reutilizar despues

# imprimir_mensaje()

# def conversacion(mensaje): #los parametros son variables que voy a tener disponibles para usarlas dentro de la funcion
#     print("hola")
#     print("como estas? ")
#     print(mensaje)
#     print("Adios")

# opcion = int(input("elige una opcion (1 , 2, 3): "))
# if opcion == 1:
#     conversacion("elegiste la opcion 1")
# elif opcion == 2:
#     conversacion("elegiste la opcion 2")
# elif opcion == 3:
#     conversacion("elegiste la opcion 3")
# else:
#     print("escribe la opcion correcta")

# if opcion == 1:
#     print("hola")
#     print("como estas?")
#     print("elegiste la opcion 1")
#     print("adios")
# elif opcion == 2:
#     print("hola")
#     print("como estas?")
#     print("elegiste la opcion 2")
#     print("adios")
# elif opcion == 3:
#     print("hola")
#     print("como estas?")
#     print("elegiste la opcion 3")
#     print("adios")
# else:
#     print("escribe la opcion correcta")

# print("mensaje especial: ")
# print("estoy aprendiendo a usar funciones")
# print("mensaje especial: ")
# print("estoy aprendiendo a usar funciones")
# print("mensaje especial: ")
# print("estoy aprendiendo a usar funciones")


########## nueva metodo para guardar el resultado de una funcion 

def suma(a, b):
    print("se suman dos numeros: ")
    resultado = a + b
    return  resultado  #utilizamos retur para devolver el resultado de la variable resultado
#es decir, con este return cuando la funcion se termine de ejecutar la variable va a ser regresada

sumatoria = suma(1, 4) #esta variable sumatoria va a ser igual al resultado de ejecutar esa funcion y esa informacion la vamos a guardar dentro de la variable sumatoria
print(sumatoria) #esto deberia devolverme 5

##NOTA : LAS FUNCIONES DEBEN ESTER POR ENCIMA DEL CODIGO PARA QUE NO HAYA PROBLEMAS AL MOMENTO DE EJECUTARLAS 