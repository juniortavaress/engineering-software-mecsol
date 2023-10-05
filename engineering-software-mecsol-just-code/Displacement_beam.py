import numpy as np
import matplotlib.pyplot as plt
from fem_data_beam import Fem_data_beam

def Displacement_beam(U, z, mx):
    # Obtendo os dados do problema de elementos finitos
    nume, neq, numnp, ee, area, Izz, h, coord, id, no = Fem_data_beam(z)

    # Inicialização dos vetores coordenadas, na configuração inicial
    xx = np.zeros((mx+1, nume))
    yy = np.zeros((mx+1, nume))

    # Inicialização dos vetores deslocamentos no sistema global
    ug = np.zeros((mx+1, nume))
    vg = np.zeros((mx+1, nume))
    uv_max = np.zeros((mx+1, nume))

    # Para cada elemento
    z1 = 0
    for n in range(nume):
        # Obtendo a incidência nodal do n-ésimo elemento
        i1 = no[0, n] -1
        i2 = no[1, n] -1

        # Obtendo as coordenadas dos nós do n-ésimo elemento
        x1 = coord[0, i1]
        y1 = coord[1, i1]
        x2 = coord[0, i2]
        y2 = coord[1, i2]

        # Determinação do comprimento do n-ésimo elemento (treliça)
        length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # Determinação do cosseno e seno do ângulo entre a barra e o eixo x global (c, s)
        c = (x2 - x1) / length
        s = (y2 - y1) / length

        # Inicialização da matriz de rotação, associada à mudança de base
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
        nodes = no.shape[0]
        lm = np.zeros(3 * nodes, dtype=int)
        for ii in range(nodes):
            in_ = no[ii, n] - 1
            lm[3 * ii] = id[0, in_]
            lm[3 * ii + 1] = id[1, in_]
            lm[3 * ii + 2] = id[2, in_]

        # Obtendo os deslocamentos e rotações (u, v, teta) dos nós do elemento finito no sistema de coordenadas global
        ns = len(lm)
        uegl = np.zeros(ns)
        for j in range(ns):
            jj = lm[j]
            if jj > 0:
                uegl[j] = U[jj - 1]

        # Determinação dos deslocamentos e rotações nos nós do n-ésimo elemento em relação ao sistema de coordenadas local
        ueloc = np.dot(Re, uegl)

        # Determinação de uma malha de valores da componente Sig[xx](x, y) para ser plotado
        tal = -1.0
        Dtal = 2 / mx

        for i in range(mx + 1):
            # Determinação da coordenada local x(tal)
            xx[i, n] = x1 * 0.5 * (1 - tal) + x2 * 0.5 * (1 + tal)
            yy[i, n] = y1 * 0.5 * (1 - tal) + y2 * 0.5 * (1 + tal)

            # Determinação do deslocamento axial e transversal no sistema local
            ul = ueloc[0] * 0.5 * (1 - tal) + ueloc[3] * 0.5 * (1 + tal)

            # Determinação das funções de interpolação para o deslocamento transversal
            nv = np.zeros(4)
            nv[0] = 0.25 * (1.0 - tal) * (1.0 - tal) * (2.0 + tal)
            nv[1] = length * (1.0 - tal) * (1.0 - tal) * (1.0 + tal) / 8.0
            nv[2] = 0.25 * (1.0 + tal) * (1.0 + tal) * (2.0 - tal)
            nv[3] = -length * (1.0 + tal) * (1.0 + tal) * (1.0 - tal) / 8.0

            # Determinação do deslocamento transversal em x(tal) sistema local
            vl = ueloc[1] * nv[0] + ueloc[2] * nv[1] + ueloc[4] * nv[2] + ueloc[5] * nv[3]

            # Determinação das componentes globais
            ug[i, n] = c * ul - s * vl
            vg[i, n] = s * ul + c * vl

            # Determinação da nova coordenada tal
            tal += Dtal

        # Determinação do deslocamento máximo
        uv_max[:, n] = np.sqrt(ug[:, n] ** 2 + vg[:, n] ** 2)
        dispNorm = np.max(uv_max)

        scaleFact = 1000 * dispNorm

        # Determinação dos vetores coordenadas na configuração deformada
        xu = xx + scaleFact * ug
        yv = yy + scaleFact * vg

        # Imprimir o maior deslocamento em magnitude em toda a estrutura
    print("Magnitude máxima do deslocamento em toda a estrutura =", dispNorm)
    print("")

    # Plotar configuração deformada da estrutura completa
    fig = plt.figure(num='Estrutura Completa')
    ax = fig.add_subplot(1, 1, 1) 
    
    for n in range(nume):
        ax.plot(xu[:, n], yv[:, n], '-')
        ax.plot(xx[:, n], yy[:, n], '--')
    ax.set_title("Estrutura Completa - Deformada e Originallllll")
    print("xx", xx)
    
    plt.show()


    return z1
