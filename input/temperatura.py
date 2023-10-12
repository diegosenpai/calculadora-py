from conversor import temperatura as temp
from excepciones import ExcepcionMenu
def subMenuTemperatura():    
    menuTmp = 0
    while True:
        try:
            print("::: Conversor Temperatura :::")
            print("1. Convertir Grados Celsius a Grados Farenheit")
            print("2. Convertir Grados Farenheit a Grados Celsius")
            opcionTmp = input(">>Ingrese su opcion \n")
            menuTmp = int(opcionTmp)
            break
        except ValueError as tmpError:
            print(f"El valor ingresado {opcionTmp} no es válido. " )
    if menuTmp == 1:
        gradosCelsius = float(input("Ingrese la temperatura en grados celsius:\n"))
        gradosFarenheit = temp.convertirCelsiusAFarenheit(gradosCelsius)
        print(f"{gradosCelsius:.2f} grados celsius equivalen a {gradosFarenheit:.2f} grados farenheit")
    if menuTmp == 2:
        gradosFarenheit = float(input("Ingrese la temperatura en grados farenheit:\n"))
        gradosCelsius = temp.convertirFarenheitACelsius(gradosFarenheit)
        print(f"{gradosFarenheit:.2f} grados farenheit equivalen a {gradosCelsius:.2f} grados celsius")
    else:
        mensaje = "Sub-Menu Temperatura: {0} es un valor incorrecto"
        raise ExcepcionMenu(mensaje.format(menuTmp))