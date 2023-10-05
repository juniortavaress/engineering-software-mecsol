import numpy as np
from calculationsCodes.fem_data_beam import Fem_data_beam

def stress_beam(disp, z, n, mx, my):
    # Obtenção dos dados do problema de elementos finitos
    nume, neq, numnp, ee, area, Izz, h, coord, id, no = Fem_data_beam(z)

    # Obtenção da incidência nodal do n-ésimo elemento
    i1 = no[0, n-1]
    i2 = no[1, n-1]

    # Obtenção das coordenadas dos nós do n-ésimo elemento
    x1 = coord[0, i1-1]
    y1 = coord[1, i1-1]
    x2 = coord[0, i2-1]
    y2 = coord[1, i2-1]

    # Determinação do comprimento do n-ésimo elemento
    length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Determinação do cosseno e seno do ângulo entre a barra e o eixo x global
    c = (x2 - x1) / length
    s = (y2 - y1) / length

    # Inicialização da matriz de rotação, associada à mudança de base, para zero
    Re = np.zeros((6, 6))

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

    # Construção do vetor de conectividade do elemento
    nodes = len(no)
    lm = np.zeros(3 * nodes, dtype=int)
    for ii in range(nodes):
        in_ = no[ii, n-1]
        lm[3*ii] = id[0, in_-1]
        lm[3*ii+1] = id[1, in_-1]
        lm[3*ii+2] = id[2, in_-1]

    # Obtenção dos deslocamentos e rotações (u, v, teta) dos nós do elemento finito no sistema de coordenadas global
    ns = len(lm)
    uegl = np.zeros(ns)
    for j in range(ns):
        jj = lm[j]
        if jj > 0:
            uegl[j] = disp[jj-1]

    # Determinação dos deslocamentos e rotações nos nós do n-ésimo elemento com relação ao sistema de coordenadas local
    ueloc = np.dot(Re, uegl)

    # Determinação de uma malha de valores da componente Sig[xx](x, y) para ser plotado
    tal = -1.0
    Dtal = 2 / mx
    dh = h / my
    y = -h / 2
    yy = np.zeros(my+1)
    xx = np.zeros(mx+1)

    for j in range(my+1):
        yy[j] = y
        y += dh

    # Inicialização dos vetores Nex, Mex e Vex
    Nex = np.zeros(mx+1)
    Mex = np.zeros(mx+1)
    Vex = np.zeros(mx+1)

    # Inicialização da matriz de tensão equivalente de von Mises
    sig = np.zeros((mx+1, my+1))

    # Para cada coordenada x em [0, length]
    for i in range(mx+1):
        x = (1 + tal) * length / 2.0
        xx[i] = x

        # Determinação do vetor Bu em x(tal)
        Bu = np.array([-1 / length, 0.0, 0.0, 1 / length, 0.0, 0.0])

        # Determinação da derivada do deslocamento axial em x(tal)
        DuDx = np.dot(Bu, ueloc)

        # Determinação do esforço normal em x(tal)
        Nx = ee * area * DuDx
        Nex[i] = Nx

        # Determinação do vetor Bv
        Bv = np.array([0.0, (4.0 / (length ** 2)) * 1.5 * tal,
                      (4.0 / (length ** 2)) * (0.75 * length * tal - 0.25 * length), 0.0,
                      -(4.0 / (length ** 2)) * 1.5 * tal,
                      (4.0 / (length ** 2)) * (0.75 * length * tal + 0.25 * length)])

        # Determinação da segunda derivada do deslocamento transversal em x(tal)
        D2vDx2 = np.dot(Bv, ueloc)

        # Determinação do momento fletor em x(tal)
        Mx = ee * Izz * D2vDx2
        Mex[i] = Mx

        # Determinação do vetor Cv(x(tal))
        cv = np.array([0.0, (8.0 * ee * Izz * 1.5) / (length ** 3),
                       (8.0 * ee * Izz * 0.75) / (length ** 2), 0.0,
                      -(8.0 * ee * Izz * 1.5) / (length ** 3),
                       (8.0 * ee * Izz * 0.75) / (length ** 2)])

        # Determinação do esforço cortante
        Vx = np.dot(cv, ueloc)
        Vex[i] = Vx

        # Para cada coordenada y em [-h/2, h/2]
        for j in range(my+1):
            y = yy[j]

            # Componente Sig(yy)
            Sxx = Nx / area - Mx * y / Izz

            # Componente Sig(xy)
            Sxy = (Vx / (2.0 * Izz)) * (0.25 * h ** 2 - y ** 2)

            # Determinação das tensões principais
            lb1 = 0.5 * Sxx + 0.5 * np.sqrt(Sxx * Sxx + 4.0 * Sxy * Sxy)
            lb2 = 0.5 * Sxx - 0.5 * np.sqrt(Sxx * Sxx + 4.0 * Sxy * Sxy)
            lb3 = 0.0

            # Determinação da tensão equivalente de von Mises
            sig[i, j] = np.sqrt((lb1 - lb2) ** 2 + (lb1 - lb3) ** 2 + (lb2 - lb3) ** 2) / np.sqrt(2.0)
        
        # Determinação da nova coordenada tal
        tal += Dtal

    return xx, yy, sig, Nex, Mex, Vex
