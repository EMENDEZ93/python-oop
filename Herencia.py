class ObjectA:
    def __init__(self, parametro):
        self.parametro = parametro

    def get_parametro(self):
        return self.parametro


class ObjectB(ObjectA):
    def __init__(self, parametro):
        super().__init__(parametro)


if __name__ == '__main__':
    objetoUno = ObjectB(parametro='ValorParametro')
    print(objetoUno.get_parametro())