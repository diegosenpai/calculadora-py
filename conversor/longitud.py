def convertirMetrosAPulagadas(valorEnMetros):
    """Transforma un valor en metros a su representaciónn en pulgadas

    Args:
        valorEnMetros (float): valor en metros

    Raises:
        ValueError: si el valor ingresado es negativo

    Returns:
        float: valor en pulgadas
    """
    if valorEnMetros >= 0:
        return valorEnMetros * 39.37
    else:
        raise ValueError("La distancia ingresada debe ser mayor a cero")
    
def convertirCentimetrosAPulgadas(valorEnCentimetros):
    """Transforma centímetros a pulgadas

    Args:
        valorEnCentimetros (valor en centimetros): valor en centiímetros

    Raises:
        ValueError: si el valor ingresado en centímetros es negativo

    Returns:
        float: valor en pulgadas
    """
    if valorEnCentimetros >= 0:
        return valorEnCentimetros / 2.54
    else:
        raise ValueError("La distancia ingresada debe ser mayor a cero")
    

def convertirKilometroAMillas(distanciaAConvertir):
    """Función que convierte kilómetros a millas

    Args:
        distanciaAConvertir (float): valor en kilómetros

    Raises:
        ValueError: si el valor en kilómetros es negativo

    Returns:
        float: valor en millas
    """
    if distanciaAConvertir >= 0:
        return distanciaAConvertir / 1.609
    else:
        raise ValueError("La distancia ingresada debe ser mayor a cero")