class MillasSinGetterSetter:
    def __init__(self, distancia=0):
        self.distancia = distancia

    def convertir_a_kilometros(self):
        return self.distancia * 1.609344


if __name__ == '__main__':
    # Creamos un nuevo objeto
    avion = MillasSinGetterSetter()

    # Indicamos la distancia
    avion.distancia = 200

    # Obtenemos el atributo distancia
    print(avion.distancia)

    # Obtenemos el método convertir_a_kilometros
    print(avion.convertir_a_kilometros())
