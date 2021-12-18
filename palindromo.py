def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

## es una buena practica de python dejar dos espacios entre las funciones y entre las funciones y el entry point
def run():  #Es una buena practica que en python nosotros tengamos una funcion que va a correr al principio
    palabra = input("escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("no es palindromo")
##entry point o punto de entrada.

if __name__ == "__main__":
    run()