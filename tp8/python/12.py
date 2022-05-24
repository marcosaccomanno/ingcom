################
# Marco - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def principal():
    '''Funcion principal'''
    contador = 0
    positivos = 0
    negativos = 0
    ceros = 0
    while contador < 10:
        x = int(input("Ingrese un numero: "))
        if x > 0:
            positivos += 1
            contador += 1
        elif x < 0:
            negativos += 1
            contador += 1
        else:
            ceros += 1
            contador += 1
    print(f"Positivos: {positivos}, Negativos: {negativos}, Ceros: {ceros}")
    
if __name__ == "__main__":
    principal()
    

