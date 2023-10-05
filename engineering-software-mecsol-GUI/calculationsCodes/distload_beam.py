import numpy as np

def distload_beam(ro, gx, gy, length, area, Izz, c, s):
    # Inicialização do vetor de força nodal equivalente associado ao peso próprio
    fel = np.zeros(6)

    # Determinação do vetor de força nodal equivalente associado ao peso próprio do elemento com relação à base local
    fel[0] = 0.5 * ro * area * gx * length
    fel[1] = 0.5 * ro * area * gy * length
    fel[2] = (ro * area * gy * length * length) / 12.0
    fel[3] = 0.5 * ro * area * gx * length
    fel[4] = 0.5 * ro * area * gy * length
    fel[5] = -(ro * area * gy * length * length) / 12.0

    # Determinação da matriz de rotação, associada à mudança de base
    Re = np.zeros((6, 6))
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

    # Determinação do vetor de força nodal equivalente associado ao peso próprio do elemento expresso na base {x,y} global
    fe = np.dot(Re.T, fel)

    return fe
