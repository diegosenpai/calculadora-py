from input import temperatura as subTemp
from input import menuLongitud as subLng
from input import menuMasa as subMasa
from input import menuVolumen as subVol
from input import menuGrados as subGrados
from excepciones import ExcepcionMenu
import os


limpiarPantalla = lambda: os.system('cls')

while True:
    print("+++++++++++ Calculadora de Conversion de Unidades +++++++++++")
    print("1. Convertir Unidades de Temperatura")
    print("2. Convertir Unidades de Longitud")
    print("3. Convertir Unidades de Masa")
    print("4. Convertir Unidades de Volumen")
    print("5. Convertir Angulos")
    print("0. Salir")
    opcionIngresada = input(">>>Ingrese su opción: \n")   
    try:
        menu = int(opcionIngresada)
        if menu == 0:
            print("Ha seleccionado salir, gracias por usar la calculadora")
            break
        if menu == 1:
            limpiarPantalla()
            subTemp.subMenuTemperatura()
        if menu == 2:
            limpiarPantalla()
            subLng.subMenuLongitud()
        if menu == 3:
            limpiarPantalla()
            subMasa.subMenuMasa()
        if menu == 4:
            limpiarPantalla()
            subVol.subMenuVolumen()
        if menu == 5:
            limpiarPantalla()
            subGrados.subMenuAngulos()

    except (ValueError,ExcepcionMenu) as error:
        print(error)
    
    
    