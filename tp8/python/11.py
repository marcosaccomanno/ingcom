################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def principal():
    '''Funcion principal'''
    z = 0
    cantidad = 0
    while z < 500:
        z_aux = int(input("Ingrese un numero: "))
        z += z_aux
        cantidad += 1
    print(f"Numeros ingresados: {cantidad}")
    
if __name__ == "__main__":
    principal()
    

