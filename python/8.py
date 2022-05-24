################
# Marco - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def calculo_promedio(nota1, nota2):
    '''
    Esta funcion toma como entrada dos numeros naturales
    y calcula su promedio.
    '''
    promedio = (nota1 + nota2) / 2
    print(f"Promedio: {promedio}")

def principal():
    '''Funcion principal'''
    par = 0 
    while par < 6:
        n1 = int(input("Nota 1: "))
        n2 = int(input("Nota 2: "))
        resultado = calculo_promedio(n1, n2)
        par +=1
    
if __name__ == "__main__":
    principal()
    




