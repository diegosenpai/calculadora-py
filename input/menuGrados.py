from conversor import angulos
from excepciones import ExcepcionMenu

def subMenuAngulos():
    """Función que despliega sub-menu para Ángulos Planos


    Raises:
        ExcepcionMenu: si la opción ingresada no corresponde a una opción válida
    """
    menuAng = 0
    while True:
        try:
            print("::: Conversor Grados :::")
            print("1. Convertir Grados a Radianes")
            print("2. Convertir Radianes a Grados")            
            opcionAng = input(">>Ingrese su opcion \n")
            menuAng = int(opcionAng)
            break
        except ValueError as error:
            print(error)
    if menuAng == 1:
        valorGrados = float(input("Ingrese el valor Grados:\n"))
        valorRadianes = angulos.convertirGradosARadianes(valorGrados)
        print(f"{valorGrados:.2f} grados equivale a {valorRadianes:.2f} radianes")
    elif menuAng ==2:
        valorRadianes = float(input("Ingrese el valor en radianes:\n"))
        valorGrados = angulos.convertirRadianesAGrados(valorRadianes)
        print(f"{valorRadianes:.2f} radianes equivale a {valorGrados:.2f} grados")    
    else:
        raise ExcepcionMenu(f"Sub-Menu Angulos: {menuAng} no es una opcion válida")