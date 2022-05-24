################
# Marco - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_par(numero):
    '''
    Esta funcion recibe como entrada un numero entero y retorna si es
    par o impar.
    '''
    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
    return resultado

def principal():
    '''Funcion principal'''
    n = int(input("Ingrese un numero: "))
    if n >= 0:
        comprobacion = es_par(n)
        print(f"{n} es {comprobacion}")

if __name__ == "__main__":
    principal()
    