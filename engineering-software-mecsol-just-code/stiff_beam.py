import numpy as np

def stiff_beam(ee, length, area, Izz, c, s):
    # Inicialização da matriz de rigidez, com relação à base local do elemento, para zero
    Ke = np.zeros((6, 6))

    # Inicialização da matriz de rotação, associada à mudança de base, para zero
    Re = np.zeros((6, 6))

    # Determinação da matriz de rigidez do elemento com relação à base local
    Ke[0, 0] = (area * ee) / length
    Ke[0, 3] = -((area * ee) / length)
    Ke[3, 0] = -((area * ee) / length)
    Ke[3, 3] = (area * ee) / length

    Ke[1, 1] = (12.0 * ee * Izz) / (length ** 3)
    Ke[1, 2] = (6.0 * ee * Izz) / (length ** 2)
    Ke[1, 4] = -((12.0 * ee * Izz) / (length ** 3))
    Ke[1, 5] = (6.0 * ee * Izz) / (length ** 2)

    Ke[2, 1] = (6.0 * ee * Izz) / (length ** 2)
    Ke[2, 2] = (4.0 * ee * Izz) / length
    Ke[2, 4] = -((6.0 * ee * Izz) / (length ** 2))
    Ke[2, 5] = (2.0 * ee * Izz) / length

    Ke[4, 1] = -((12.0 * ee * Izz) / (length ** 3))
    Ke[4, 2] = -((6.0 * ee * Izz) / (length ** 2))
    Ke[4, 4] = (12.0 * ee * Izz) / (length ** 3)
    Ke[4, 5] = -((6.0 * ee * Izz) / (length ** 2))

    Ke[5, 1] = (6.0 * ee * Izz) / (length ** 2)
    Ke[5, 2] = (2.0 * ee * Izz) / length
    Ke[5, 4] = -((6.0 * ee * Izz) / (length ** 2))
    Ke[5, 5] = (4.0 * ee * Izz) / length

    # Determinação da matriz de rotação, associada à mudança de base
    Re[0, 0] = c
    Re[0, 1] = s
    Re[1, 0] = -s
    Re[1, 1] = c
    Re[2, 2] = 1.0

    Re[3, 3] = c
    Re[3, 4] = s
    Re[4, 3] = -s
    Re[4, 4] = c
    Re[5, 5] = 1.0

    # Determinação da matriz de rigidez do elemento, expressa na base {x, y} global
    A = np.dot(Ke, Re)
    k = np.dot(Re.T, A)

    return k
