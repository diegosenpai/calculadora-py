from conversor import longitud 
from excepciones import ExcepcionMenu

def subMenuLongitud():
    """Función que despliega sub-menú para transformaciones de longitud

    Raises:
        ExcepcionMenu: si la opción ingresada no corresponde a una opción válida
    """
    menuLng = 0
    while True:
        try:
            print("::: Conversor Longitud :::")
            print("1. Convertir Metros a Pulgadas")
            print("2. Convertir Centimetros a Pulgadas")
            print("3. Convertir Kilometros a Millas")
            opcionLng = input(">>Ingrese su opcion \n")
            menuLng = int(opcionLng)
            break
        except ValueError as error:
            print(error)
    if menuLng == 1:
        valorMetros = float(input("Ingrese el valor en metros:\n"))
        valorPulgadas = longitud.convertirMetrosAPulagadas(valorMetros)
        print(f"{valorMetros:.2f} metros equivale a {valorPulgadas:.2f} pulgadas")
    elif menuLng ==2:
        valorCentimetros = float(input("Ingrese el valor en centímetros:\n"))
        valorPulgadas = longitud.convertirCentimetrosAPulgadas(valorCentimetros)
        print(f"{valorCentimetros:.2f} centimetros equivale a {valorPulgadas:.2f} pulgadas")
    elif menuLng ==3:
        valorKilometros = float(input("Ingrese el valor en kilómetros:\n"))
        valorMillas = longitud.convertirKilometroAMillas(valorKilometros)
        print(f"{valorKilometros:.2f} kilómetros equivale a {valorMillas:.2f} millas")
    else:
        raise ExcepcionMenu(f"Sub-Menu Longitud: {menuLng} no es una opcion válida") 