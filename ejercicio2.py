################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
    
    '''
    Esta funcion toma como entrada un numero real y devuelve
    el signo del mismo (positivo, negativo o neutro). 
    '''
        
    if numero == 0:
        return "neutro"
    elif numero > 0:
        return "positivo"
    else:
        return "negativo"


def principal():
    
    # entrada
    
    numero = float(input("Ingrese un numero: "))
    
    # algoritmo
    
    signo_numero = signo(numero)

    # salida

    print(f"{numero} es {signo_numero}")
    

if __name__ == "__main__":
    principal()