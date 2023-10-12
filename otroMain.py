from conversor import temperatura as temp
from conversor import longitud as lng

temperatura = temp.convertirFarenheitACelsius(98)
print(f"{temperatura:.2f}")


try:
    distanciaEnPulgadas = lng.convertirKilometroAMillas(3)
    print(f"distancia en millas: {distanciaEnPulgadas:.2f}")
except ValueError as err:
    print(err)