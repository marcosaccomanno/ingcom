################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Se solicita al usuario el ingreso de un numero real

numero = input("Ingrese un numero: ")

def compara(numero, otro_numero):
    
    '''
    Esta funcion toma como entrada dos numeros y retorna como
    salida "-1" si el primero es menor que el segundo, "0" si
    son iguales y "1" si el primero es mayor que el segundo.
    '''
    
    operacion = numero.split("+")
    numero = operacion[0]
    otro_numero = operacion[1]
    
    if numero == otro_numero:
        return 0
    elif numero > otro_numero:
        return 1
    else:
        return -1


comparacion = compara(numero, otro_numero)

print(comparacion)


def principal():
    pass

if __name__ == "__main__":
    principal()