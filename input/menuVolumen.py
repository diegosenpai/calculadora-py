from conversor import volumen
from excepciones import ExcepcionMenu

def subMenuVolumen():
    """Función que despliega sub-menú para transformaciones de volumen

    Raises:
        ExcepcionMenu: si la opción ingresada no corresponde a una opción válida
    """
    menuVol = 0
    while True:
        try:
            print("::: Conversor Volumen :::")
            print("1. Convertir Galones a Metros Cubicos")
            print("2. Convertir Litros a Galones")            
            opcionVol = input(">>Ingrese su opcion \n")
            menuVol = int(opcionVol)
            break
        except ValueError as error:
            print(error)
    if menuVol == 1:
        valorGalones = float(input("Ingrese el valor en Galones:\n"))
        valorMetros = volumen.convertirGalonesAMetrosCubicos(valorGalones)
        print(f"{valorGalones:.2f} galones equivale a {valorMetros:.2f} metros cúbicos")
    elif menuVol ==2:
        valorLitros = float(input("Ingrese el valor en litros:\n"))
        valorGalones = volumen.convertirLitrosAGalones(valorLitros)
        print(f"{valorLitros:.2f} litros equivale a {valorGalones:.2f} galones")    
    else:
        raise ExcepcionMenu(f"Sub-Menu Volumen: {menuVol} no es una opcion válida")