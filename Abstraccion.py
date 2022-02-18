class AbstraccionA:
    def __init__(self):
        pass

    def metodo_uno(self, parametro_a='valor a'):
        self._metodo_do(parametro_a)

    def _metodo_do(self, parametro_a):
        print(f'valo => {parametro_a}')


if __name__ == '__main__':
    abstracion = AbstraccionA()
    abstracion.metodo_uno()
