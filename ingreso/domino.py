# DOMINO

izquierda = 0
derecha = 0

for numero_izquierda in range(7):
    for numero_derecha in range(7):
        print(f" {izquierda} | {derecha}")
        derecha = derecha + 1
    derecha = 0
    izquierda = izquierda + 1
