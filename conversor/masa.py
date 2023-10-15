def convertirLibrasAKilos(valorEnKilos): 
    """Funcion que convierte libras a kilos

    Args:
        valorEnKilos (float): valor en Kilos

    Raises:
        ValueError: si el valor en kilos es negativo

    Returns:
        float: valor en libras
    """
    if valorEnKilos >= 0:
        return valorEnKilos / 2.205
    else:
        raise ValueError("El valor ingresado en kilos debe ser positivo")
    

def convertirKilosALibras(valorEnLibras):
    """Funcion que convierte kilos a libras

    Args:
        valorEnLibras (float): valor en kilos a transformar

    Raises:
        ValueError: si el valor en kilos es negativo

    Returns:
        float: valor en libras
    """
    if valorEnLibras > 0:
        return valorEnLibras * 2.205
    else:
        raise ValueError("El valor en libras debe ser positivo")