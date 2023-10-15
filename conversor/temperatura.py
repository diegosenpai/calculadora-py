def convertirCelsiusAFarenheit(valorTemperatura):
    """Función que transforma grados celsius a grados Farenheit

    Args:
        valorTemperatura (float): valor en grados celsius

    Returns:
        float: valor en grados farenheit
    """
    return valorTemperatura * (9/5) + 32

def convertirFarenheitACelsius(valorTemperatura):
    """Función que transforma grados Farenheit a grados celsius

    Args:
        valorTemperatura (float): valor en grados Farenheit

    Returns:
        float: valor en grados celsius
    """
    return (valorTemperatura - 32) * (5/9) 
        
  