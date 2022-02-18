def funcion_decoradora(funcion):
    def wrapper():
        print("Este es el último mensaje...")
        funcion()
        print("Este es el primer mensaje ;)")

    return wrapper


def zumbido():
    print("Buzzzzzz")


@funcion_decoradora
def zumbido_con_decorador():
    print("Buzzzzzz - Con Decorador")


if __name__ == '__main__':
    # zumbido = funcion_decoradora(zumbido)
    # zumbido()

    zumbido_con_decorador()
