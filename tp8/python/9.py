################
# Marco - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def principal():
    '''Funcion principal'''
    a = int(input("Ingrese un numero: "))
    if a % 3 == 0:
        print(f"{a} es multiplo de 3.")
    else:
        print(f"{a} no es multiplo de 3.")
    
if __name__ == "__main__":
    principal()
    



