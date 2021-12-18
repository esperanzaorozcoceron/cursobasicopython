import random #este random hace parte de un modulo, los modulos son un paquete de codigo escrito por las personas que hicieron python que nosotros tenemos disponible para poder ejecutar

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("elige un numero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("busca un numero mas grande")
        else:
            print("busca un numero mas pequeño")
        numero_elegido = int(input("elige otro numero: "))
    print("ganaste")

if __name__ == "__main__":
    run()