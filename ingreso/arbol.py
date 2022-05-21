#ARBOL

hoja = ""
tronco = "| "
espacio = " "

cantidad_espacios = int(input("Cantidad de filas: "))
cantidad_hojas = 1
espacio_tronco = cantidad_espacios - 1

while cantidad_espacios > 0:
    print(espacio cantidad_espacios + hoja * cantidad_hojas)
    cantidad_espacios = cantidad_espacios - 1
    cantidad_hojas = cantidad_hojas + 2

print(espacio * espacio_tronco + tronco * 2) 
