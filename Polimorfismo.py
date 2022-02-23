class ObjectA:
    def __init__(self, parametro):
        self.parametro = parametro

    def get_parametro(self):
        print(self.parametro)


class ObjectB(ObjectA):
    def __init__(self, parametro):
        super().__init__(parametro)

    def get_parametro(self):
        print("* polimorfismo *")


if __name__ == '__main__':
    objeto = ObjectB("ValoreParametro")
    objeto.get_parametro()