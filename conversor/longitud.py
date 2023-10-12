def convertirMetrosAPulagadas(valorEnMetros):
    if valorEnMetros >= 0:
        return valorEnMetros * 39.37
    else:
        raise ValueError("La distancia ingresada debe ser mayor a cero")
    
def convertirCentimetrosAPulgadas(valorEnCentimetros):
    if valorEnCentimetros >= 0:
        return valorEnCentimetros / 2.54
    else:
        raise ValueError("La distancia ingresada debe ser mayor a cero")
    
def convertirKilometroAMillas(distanciaAConvertir):
    if distanciaAConvertir >= 0:
        return distanciaAConvertir / 1.609
    else:
        raise ValueError("La distancia ingresada debe ser mayor a cero")