# contador = 0
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))

# contador = 1
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))

# contador = 2
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))

# contador = 3
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))

# contador = 4
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))

# contador = 5
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))

##CICLO WHILE

def run():   #primero definimos una funcion principal
    LIMITE = 1000 # Para definir una variable constante solo debemos colocar el nombre en mayusculas. Se le conoce como variable constanta ya que esta variable no va a cambiar siempre va a tener el numero 1000
    contador = 0
    potencia_dos = 2**contador
    while potencia_dos < LIMITE: #mientras la potencia de dos sea menor al limite, se va a ejecutar lo que este debajo del ciclo while
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_dos))
        contador = contador + 1
        potencia_dos = 2**contador


if __name__ == "__main__":
    run()
