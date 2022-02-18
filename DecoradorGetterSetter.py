class Millas:
    def __init__(self):
        self.__distancia = 0

    # Función para obtener el valor de _distancia
    # Usando el decorador property
    @property
    def distancia(self):
        print("Llamada al método getter")
        return self.__distancia

    # Función para definir el valor de _distancia
    @distancia.setter
    def distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        print("Llamada al método setter")
        self.__distancia = valor


if __name__ == '__main__':
    # Creamos un nuevo objeto
    avion = Millas()

    # Indicamos la distancia
    avion.distancia = 1200

    print(avion.distancia)
