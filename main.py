from conversor import temperatura as temp
import os


limpiarPantalla = lambda: os.system('cls')

while True:
    print("+++++++++++ Calculadora de Conversion de Unidades +++++++++++")
    print("1. Convertir Unidades de Temperatura")
    print("2. Convertir Unidades de Masa")
    print("3. Convertir Unidades de Distancia")
    print("4. Convertir Unidades de Capacidad")
    print("5. Convertir Angulos")
    print("0. Salir")
    opcionIngresada = print(">>>Ingrese su opción: \n")
    if opcionIngresada.isdigit():
        menu = int(opcionIngresada)
        if menu == 0:
            print("Ha seleccionado salir, gracias por usar la calculadora")
            break
        if menu == 1:
            limpiarPantalla()
            print("Convertir Temperatura")
            while True:
                print("1. Convertir Grados Celsius a Grados Farenheit")
                print("2. Convertir Grados Farenheit a Grados Celsius")
                opcionTemperatura = input("Ingrese la operacion a realizar: \n")
                if opcionTemperatura.isdigit():
                    menuTemperatura = int(opcionTemperatura)
                    if menuTemperatura == 1:
                    else:
                        print(f"La opcion {opcionTemperatura} ingresada no es valida")
                else:
                    print(f"El valor ingresado no es una opción válida.")
            
    else:
        print(f"El valor ingresado {opcionIngresada} no es un valor valido. Intentelo nuevamente")
    
    
    