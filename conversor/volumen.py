
def convertirGalonesAMetrosCubicos(valorEnGalones):
    if valorEnGalones >= 0:
        return valorEnGalones / 264.2
    else:
        raise ValueError("El valor en galones debe ser positivo")
    
def convertirLitrosAGalones(valorEnLitros):
    if valorEnLitros >= 0:
        return valorEnLitros / 4.546
    else:
        raise ValueError("El valor en litros debe ser positivo")