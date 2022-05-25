################
# Marco - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def multiplicacion_lenta(multiplicando, multiplicador):
    '''
    Esta funcion toma como entrada dos numeros naturales y realiza la multiplicacion
    entre ambos mediante sumas.
    '''
    contador = 0
    resultado = 0
    while contador < multiplicador:
        resultado += multiplicando
        contador += 1
    return resultado

def principal():
    '''Funcion principal'''
    p = int(input("Ingrese el multiplicando: "))
    q = int(input("Ingrese el multiplicador: "))
    operacion = multiplicacion_lenta(p, q)
    print(f"p = {p}, q = {q}")
    print(f"p * q = {operacion}")

if __name__ == "__main__":
    principal()
    