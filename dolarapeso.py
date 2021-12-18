dolares = input("¿cuantos dolares tienes?: ")
dolares = float(dolares)
valor_pesos = 3875
pesos = dolares * valor_pesos
pesos = round(pesos, 2)  #con el comando round lo que hago es redondear la variable que quiero y especifico la cantidad que quiero que redondee
pesos = str(pesos)
print("tienes $" + pesos + " pesos")