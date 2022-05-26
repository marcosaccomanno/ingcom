################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def intervalo(numero):
    if numero >= -1 and numero < 0:
        resultado = "pertenece al intervalo [-1; 0)"
    elif numero > 0 and numero <= 1:
        resultado = "pertenece al intervalo (0; 1]"
    else:
        resultado = "no pertenece a ninguno de los intervalos"
    return resultado

def principal():
    '''Funcion principal'''
    x = float(input("Ingrese un numero: "))
    que_intervalo = intervalo(x)
    print(f"{x} {que_intervalo}")

if __name__ == "__main__":
    principal()
    
