from conversor import masa 
from excepciones import ExcepcionMenu

def subMenuMasa():
    menuMasa = 0
    while True:
        try:
            print("::: Conversor Masa :::")
            print("1. Convertir Libras a Kilos")
            print("2. Convertir Kilos a Libras")            
            opcionMasa = input(">>Ingrese su opcion \n")
            menuMasa = int(opcionMasa)
            break
        except ValueError as error:
            print(error)
    if menuMasa == 1:
        valorLibras = float(input("Ingrese el valor en Libras:\n"))
        valorKilos = masa.convertirLibrasAKilos(valorLibras)
        print(f"{valorLibras:.2f} libras equivale a {valorKilos:.2f} kilos")
    elif menuMasa ==2:
        valorKilos = float(input("Ingrese el valor en kilos:\n"))
        valorLibras = masa.convertirKilosALibras(valorKilos)
        print(f"{valorKilos:.2f} kilos equivale a {valorLibras:.2f} libras")    
    else:
        raise ExcepcionMenu(f"Sub-Menu Longitud: {menuMasa} no es una opcion válida") 