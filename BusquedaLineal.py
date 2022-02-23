import random


def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break
        return match


if __name__ == '__main__':
    tamano_lista = int(input('Tamaños Lista'))
    objectivo = int(input("Buscar"))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    match = busqueda_lineal(lista, objectivo)
    print(lista)
    print(f'Elemento {objectivo} {"esta" if match else "no esta"} en la lista')