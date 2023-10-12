# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:31:56 2023

@author: CEC
"""

def convertirLibrasAKilos(valorEnKilos):    
    if valorEnKilos >= 0:
        return valorEnKilos / 2.205
    else:
        raise ValueError("El valor ingresado en kilos debe ser positivo")
    

def convertirKilosALibras(valorEnLibras):
    if valorEnLibras > 0:
        return valorEnLibras * 2.205
    else:
        raise ValueError("El valor en libras debe ser positivo")