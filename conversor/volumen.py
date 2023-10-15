
def convertirGalonesAMetrosCubicos(valorEnGalones):
    """Funcion que transforma galones a metros cubicos

    Args:
        valorEnGalones (float): valor en galones

    Raises:
        ValueError: si el valor en galones es negativo

    Returns:
        float: valor en metros cubicos
    """
    if valorEnGalones >= 0:
        return valorEnGalones / 264.2
    else:
        raise ValueError("El valor en galones debe ser positivo")
    
def convertirLitrosAGalones(valorEnLitros):
    """Funcion que transforma litros a galones

    Args:
        valorEnLitros (float): valor en litros

    Raises:
        ValueError: si el valor de litros es negativo

    Returns:
        float: valor en galones
    """
    if valorEnLitros >= 0:
        return valorEnLitros / 4.546
    else:
        raise ValueError("El valor en litros debe ser positivo")