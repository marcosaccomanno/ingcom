def calculo_porcentaje(numero, porcentaje):
    '''
    Esta funcion toma como entrada un numero y un porcentaje
    y retorna el valor de ese porcentaje del numero. 
    '''
    return numero * porcentaje / 100

def agregar_porcentaje(numero, porcentaje):
    '''
    Esta funcion toma como entrada un numero y un porcentaje.
    Suma el porcentaje al numero y retorna el resultado.
    '''
    return numero + numero * porcentaje / 100

def restar_porcentaje(numero, porcentaje):
    '''
    Esta funcion toma como entrada un numero y un porcentaje.
    Resta el porcentaje al numero y retorna el resultado.
    '''
    return numero - numero * porcentaje / 100

def que_porcentaje(numero, segundo_numero):
    '''
    Esta funcion toma como entrada dos numeros y retorna que porcentaje
    del primer numero representa el segundo numero.
    '''
    return segundo_numero * 100 / numero


def main():
    
    print("___________________________________________________________________________")
    print("*Para calcular el porcentaje de un numero ingrese 1")
    print("*Para sumar un porcentaje a un numero ingrese 2")
    print("*Para restar un porcentaje a un numero ingrese 3")
    print("*Para saber que porcentaje de un numero representa otro numero ingrese 4")
    print("*Para salir ingrese 0")
    print("___________________________________________________________________________")
    
   
    while True:
        opcion = int(input("Opcion: "))
    
        if opcion == 1:
            numero = float(input("Numero: "))
            porcentaje = float(input("Porcentaje: "))
            resultado_porcentaje = calculo_porcentaje(numero, porcentaje)
            print(f"* El {porcentaje}% de {numero} es {resultado_porcentaje}")
            
        elif opcion == 2:
            numero = float(input("Numero: "))
            porcentaje = float(input("Porcentaje: "))
            porcentaje_agregado = agregar_porcentaje(numero, porcentaje)
            print(f"* {numero} + el {porcentaje}% es {porcentaje_agregado}")
            
        elif opcion == 3:
            numero = float(input("Numero: "))
            porcentaje = float(input("Porcentaje: "))
            porcentaje_restado = restar_porcentaje(numero, porcentaje)
            print(f"* {numero} - el {porcentaje}% es {porcentaje_restado}")
            
        elif opcion == 4:
            numero = float(input("Numero: "))
            segundo_numero = float(input("Segundo numero: "))
            valor_porcentaje = que_porcentaje(numero, segundo_numero)
            print(f"* {segundo_numero} es el {valor_porcentaje}% de {numero}")
            
        elif opcion == 0:
            break
            
        else:
            print(f"{opcion} no es una opcion valida.")
        
    
    
if __name__ == "__main__":
    main()