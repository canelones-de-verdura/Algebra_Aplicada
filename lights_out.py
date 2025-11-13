from math import sqrt
from random import randint


# es más sencillo trabajar con vectores de tamaño nxn que con arrays de dos dimensiones
def generar_matriz(n):
    return [randint(0, 1) for _ in range(n**2)]


def generar_sistema(matriz):
    # para un tablero de nxn, el sistema de la solución (matriz aumentada) queda (n*n) x ((n*n)+1)
    n = sqrt(len(matriz))

    # lado derecho de la igualdad
    b = [1 if celda == 1 else 0 for celda in matriz]

    '''
    lado izquierdo
    siguiendo el ejemplo de la letra:
      x1 + x2 + x4 = 0
      x1 + x2 + x3 + x5 = 1
      x2 + x3 + x6 = 0
      ...

    es igual a 
      x1 + x2 + 0*x3 + x4 + 0*x5 + 0*x6 + 0*x7 + 0*x8 + 0*x9 = 0 
      x1 + x2 + x3 + 0*x4 + x5 + 0*x6 + 0*x7 + 0*x8 + 0*x9 = 1 
      0*x1 + x2 + x3 + 0*x4 + 0*x5 + x6 + 0*x7 + 0*x8 + 0*x9 = 0
      ...

    entonces la matrix extendida queda
      1 1 0 1 0 0 0 0 0 | 0
      1 1 1 0 1 0 0 0 0 | 1
      0 1 1 0 0 1 0 0 0 | 0
      ...
    '''

    a = [[0 for _ in range(len(matriz))] for _ in range(len(matriz))]



    return a, b


if __name__ == "__main__":
    n = int(input("Ingresar tamaño de matriz n*n:\n\t> "))

    print(generar_sistema(generar_matriz(n)))
