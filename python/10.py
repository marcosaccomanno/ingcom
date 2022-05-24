################
# Marco - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def principal():
    '''Funcion principal'''
    b = int(input("Ingrese un numero: "))
    cantidad = 0
    while b > 0:
        cantidad += 1
        b = int(input("Ingrese un numero: "))
    print(f"Numeros ingresados: {cantidad}")
    
if __name__ == "__main__":
    principal()
    

